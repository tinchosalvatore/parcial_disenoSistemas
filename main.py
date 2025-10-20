import time
from datetime import date, timedelta

# Entidades
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.apto_medico import AptoMedico
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.personal.herramienta import Herramienta

# Servicios
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.personal.trabajador_service import TrabajadorService
from python_forestacion.servicios.negocio.fincas_service import FincasService

# Riego y Sensores
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask

# Constantes
from python_forestacion.constantes import THREAD_JOIN_TIMEOUT, DURACION_TAREA_REGAR, DURACION_TAREA_COSECHAR


def run_simulation():
    """Función principal que orquesta la simulación completa."""
    print("*** INICIANDO SIMULACIÓN DE GESTIÓN FORESTAL ***")

    # 1. Instanciar todos los servicios
    registro_service = RegistroForestalService()
    plantacion_service = PlantacionService()
    tierra_service = TierraService()
    trabajador_service = TrabajadorService()
    fincas_service = FincasService()

    # 2. Crear el Registro Forestal
    print("\n--- Creando la finca ---")
    registro = registro_service.crear_registro(
        propietario="Juan Perez",
        codigo_catastral="ABC-123",
        sup_tierra=10000.0,
        sup_plantacion=5000.0
    )
    plantacion = registro.get_plantacion()
    plantacion.set_agua_disponible(500.0) # Añadir agua al depósito

    # 3. Plantar cultivos
    print("\n--- Plantando cultivos ---")
    try:
        plantacion_service.plantar(plantacion, "Pino", 10)
        plantacion_service.plantar(plantacion, "Olivo", 5)
        plantacion_service.plantar(plantacion, "Lechuga", 20)
        plantacion_service.plantar(plantacion, "Zanahoria", 30)
    except Exception as e:
        print(f"Error al plantar: {e}")

    registro_service.mostrar_datos(registro, tierra_service, plantacion_service)

    # 4. Crear y asignar trabajadores
    print("\n--- Contratando y asignando personal ---")
    trabajador1 = Trabajador("Carlos", "Gomez", "30123456")
    apto_medico = AptoMedico(date.today(), date.today() + timedelta(days=365), True)
    trabajador_service.asignar_apto_medico(trabajador1, apto_medico)
    trabajador1.asignar_tarea(Tarea("Regar", DURACION_TAREA_REGAR))
    trabajador1.asignar_tarea(Tarea("Cosechar", DURACION_TAREA_COSECHAR))
    plantacion.agregar_trabajador(trabajador1)
    trabajador_service.mostrar_datos(trabajador1)

    # 5. Iniciar sistema de riego automatizado
    print("\n--- Iniciando sistema de riego automatizado ---")
    temp_task = TemperaturaReaderTask()
    hum_task = HumedadReaderTask()
    control_task = ControlRiegoTask(plantacion_service, plantacion)

    # Suscribir el control a los sensores
    temp_task.agregar_observador(control_task)
    hum_task.agregar_observador(control_task)

    # Iniciar hilos
    temp_task.start()
    hum_task.start()
    control_task.start()

    # 6. Simular el paso del tiempo
    print("\n--- Simulación en curso (10 segundos) ---")
    time.sleep(10)

    # 7. Realizar más operaciones
    print("\n--- Realizando operaciones adicionales ---")
    trabajador_service.trabajar(trabajador1, date.today(), Herramienta("Pala", "Manual"))
    try:
        fincas_service.fumigar(plantacion)
    except Exception as e:
        print(f"Error al fumigar: {e}")

    # 8. Cosechar y empaquetar
    print("\n--- Cosechando y empaquetando ---")
    paquetes = fincas_service.cosechar_y_empaquetar(plantacion)
    print(f"Se generaron {len(paquetes)} paquetes en total.")

    # 9. Persistir el estado final
    print("\n--- Guardando estado de la finca ---")
    try:
        registro_service.persistir_registro(registro)
    except Exception as e:
        print(f"Error al persistir: {e}")

    # 10. Detener hilos
    print("\n--- Deteniendo sistema de riego ---")
    temp_task.detener()
    hum_task.detener()
    control_task.detener()
    temp_task.join(THREAD_JOIN_TIMEOUT)
    hum_task.join(THREAD_JOIN_TIMEOUT)
    control_task.join(THREAD_JOIN_TIMEOUT)
    print("Hilos detenidos.")

    # 11. Verificar persistencia
    print("\n--- Verificando la persistencia ---")
    try:
        registro_leido = registro_service.leer_registro("Juan Perez")
        registro_service.mostrar_datos(registro_leido, tierra_service, plantacion_service)
    except Exception as e:
        print(f"Error al leer el registro: {e}")
    
    print("\n*** SIMULACIÓN COMPLETADA EXITOSAMENTE ***")

if __name__ == "__main__":
    run_simulation()
