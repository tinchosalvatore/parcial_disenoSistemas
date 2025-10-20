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

# Excepciones
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.excepciones.persistencia_exception import PersistenciaException


def run_simulation():
    """Función principal que orquesta la simulación completa."""
    print("======================================================================")
    print("         SISTEMA DE GESTION FORESTAL - PATRONES DE DISENO")
    print("======================================================================")

    # 1. Instanciar todos los servicios
    print("\n----------------------------------------------------------------------")
    print("  PATRON SINGLETON: Inicializando servicios")
    print("----------------------------------------------------------------------")
    
    registro_service = RegistroForestalService()
    plantacion_service = PlantacionService()
    tierra_service = TierraService()
    trabajador_service = TrabajadorService()
    fincas_service = FincasService()
    
    print("[OK] Todos los servicios comparten la misma instancia del Registry")

    # 2. Crear el Registro Forestal
    print("\n1. Creando tierra con plantacion...")
    registro = registro_service.crear_registro(
        propietario="Juan Perez",
        codigo_catastral="ABC-123",
        sup_tierra=10000.0,
        sup_plantacion=5000.0
    )
    plantacion = registro.get_plantacion()
    plantacion.set_agua_disponible(500.0)  # Añadir agua al depósito
    print("[OK] Registro forestal creado exitosamente")

    # 3. Plantar cultivos usando Factory Method
    print("\n----------------------------------------------------------------------")
    print("  PATRON FACTORY: Creacion de cultivos")
    print("----------------------------------------------------------------------")
    print("2. Plantando cultivos (via Factory Method)...")
    
    try:
        plantacion_service.plantar(plantacion, "Pino", 10)
        plantacion_service.plantar(plantacion, "Olivo", 5)
        plantacion_service.plantar(plantacion, "Lechuga", 20)
        plantacion_service.plantar(plantacion, "Zanahoria", 30)
        print("[OK] 65 cultivos plantados exitosamente")
    except SuperficieInsuficienteException as e:
        print(f"[ERROR] {e.get_user_message()}")
        return

    # 4. Mostrar datos iniciales del registro
    print("\n3. Estado inicial de la finca:")
    registro_service.mostrar_datos(registro, tierra_service, plantacion_service)

    # 5. Crear y asignar trabajadores
    print("\n----------------------------------------------------------------------")
    print("  GESTION DE PERSONAL: Trabajadores y tareas")
    print("----------------------------------------------------------------------")
    print("4. Contratando y asignando personal...")
    
    trabajador1 = Trabajador("Carlos", "Gomez", "30123456")
    apto_medico = AptoMedico(date.today(), date.today() + timedelta(days=365), True)
    trabajador_service.asignar_apto_medico(trabajador1, apto_medico)
    trabajador1.asignar_tarea(Tarea("Regar", DURACION_TAREA_REGAR))
    trabajador1.asignar_tarea(Tarea("Cosechar", DURACION_TAREA_COSECHAR))
    plantacion.agregar_trabajador(trabajador1)
    
    print(f"[OK] Trabajador {trabajador1.get_nombre_completo()} contratado")
    trabajador_service.mostrar_datos(trabajador1)

    # 6. Iniciar sistema de riego automatizado (Patron Observer)
    print("\n----------------------------------------------------------------------")
    print("  PATRON OBSERVER: Sistema de riego automatizado")
    print("----------------------------------------------------------------------")
    print("5. Iniciando sensores y control de riego...")
    
    temp_task = TemperaturaReaderTask()
    hum_task = HumedadReaderTask()
    control_task = ControlRiegoTask(plantacion_service, plantacion)

    # Suscribir el control a los sensores (Observer Pattern)
    temp_task.agregar_observador(control_task)
    hum_task.agregar_observador(control_task)

    # Iniciar hilos daemon
    temp_task.start()
    hum_task.start()
    control_task.start()
    print("[OK] Sistema de riego automatizado iniciado (3 threads daemon)")

    # 7. Simular el paso del tiempo
    print("\n----------------------------------------------------------------------")
    print("  SIMULACION: Sistema en funcionamiento")
    print("----------------------------------------------------------------------")
    print("6. Simulacion en curso (10 segundos)...")
    print("   - Sensores leyendo temperatura y humedad")
    print("   - Control de riego evaluando condiciones")
    print("   - Estrategia de absorcion aplicandose segun cultivo")
    time.sleep(10)
    print("[OK] Simulacion completada")

    # 8. Realizar operaciones adicionales
    print("\n----------------------------------------------------------------------")
    print("  OPERACIONES DE NEGOCIO")
    print("----------------------------------------------------------------------")
    print("7. Trabajador ejecutando tareas...")
    
    herramienta = Herramienta("Pala", "Manual")
    resultado_trabajo = trabajador_service.trabajar(trabajador1, date.today(), herramienta)
    
    if resultado_trabajo:
        print(f"[OK] {trabajador1.get_nombre_completo()} completo sus tareas")
    else:
        print(f"[WARN] {trabajador1.get_nombre_completo()} no pudo trabajar")

    print("\n8. Fumigando plantacion...")
    try:
        fincas_service.fumigar(plantacion)
        print("[OK] Fumigacion completada")
    except AguaAgotadaException as e:
        print(f"[WARN] {e.get_user_message()}")

    # 9. Cosechar y empaquetar
    print("\n9. Cosechando y empaquetando...")
    paquetes = fincas_service.cosechar_y_empaquetar(plantacion)
    print(f"[OK] Se generaron {len(paquetes)} paquetes en total")

    # 10. Persistir el estado final
    print("\n----------------------------------------------------------------------")
    print("  PERSISTENCIA: Guardando estado")
    print("----------------------------------------------------------------------")
    print("10. Guardando estado de la finca...")
    
    try:
        registro_service.persistir_registro(registro)
        print("[OK] Registro persistido exitosamente")
    except PersistenciaException as e:
        print(f"[ERROR] {e.get_user_message()}")
        print(f"        Detalle tecnico: {e.get_tech_message()}")

    # 11. Detener hilos de forma segura
    print("\n----------------------------------------------------------------------")
    print("  DETENCION SEGURA: Finalizando threads")
    print("----------------------------------------------------------------------")
    print("11. Deteniendo sistema de riego...")
    
    temp_task.detener()
    hum_task.detener()
    control_task.detener()
    
    temp_task.join(THREAD_JOIN_TIMEOUT)
    hum_task.join(THREAD_JOIN_TIMEOUT)
    control_task.join(THREAD_JOIN_TIMEOUT)
    print("[OK] Todos los hilos detenidos correctamente")

    # 12. Verificar persistencia
    print("\n----------------------------------------------------------------------")
    print("  VERIFICACION: Lectura de datos persistidos")
    print("----------------------------------------------------------------------")
    print("12. Verificando la persistencia...")
    
    try:
        registro_leido = RegistroForestalService.leer_registro("Juan Perez")
        print("[OK] Registro recuperado exitosamente")
        print("\n13. Estado final de la finca (desde disco):")
        registro_service.mostrar_datos(registro_leido, tierra_service, plantacion_service)
    except PersistenciaException as e:
        print(f"[ERROR] {e.get_user_message()}")
    
    # Mensaje final de exito
    print("\n======================================================================")
    print("              EJECUCION COMPLETADA EXITOSAMENTE")
    print("======================================================================")
    print("  [OK] SINGLETON   - CultivoServiceRegistry (instancia unica)")
    print("  [OK] FACTORY     - Creacion de cultivos")
    print("  [OK] OBSERVER    - Sistema de sensores y eventos")
    print("  [OK] STRATEGY    - Algoritmos de absorcion de agua")
    print("======================================================================")
    print("\nEl sistema demostro exitosamente:")
    print("  - Plantacion de 4 tipos de cultivos")
    print("  - Riego automatizado basado en sensores")
    print("  - Gestion de trabajadores con apto medico")
    print("  - Operaciones de negocio (fumigar, cosechar)")
    print("  - Persistencia y recuperacion de datos")
    print("  - Threading seguro con graceful shutdown")
    print("======================================================================")


if __name__ == "__main__":
    try:
        run_simulation()
    except KeyboardInterrupt:
        print("\n[INTERRUPT] Simulacion interrumpida por el usuario")
    except Exception as e:
        print(f"\n[ERROR CRITICO] Ocurrio un error inesperado: {e}")
        import traceback
        traceback.print_exc()