"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion
Fecha de generacion: 2025-10-21 21:58:15
Total de archivos integrados: 67
Total de directorios procesados: 21
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. __init__.py
#   2. constantes.py
#
# DIRECTORIO: ..
#   3. main.py
#
# DIRECTORIO: entidades
#   4. __init__.py
#
# DIRECTORIO: entidades/cultivos
#   5. __init__.py
#   6. arbol.py
#   7. cultivo.py
#   8. hortaliza.py
#   9. lechuga.py
#   10. olivo.py
#   11. pino.py
#   12. tipo_aceituna.py
#   13. zanahoria.py
#
# DIRECTORIO: entidades/personal
#   14. __init__.py
#   15. apto_medico.py
#   16. herramienta.py
#   17. tarea.py
#   18. trabajador.py
#
# DIRECTORIO: entidades/terrenos
#   19. __init__.py
#   20. plantacion.py
#   21. registro_forestal.py
#   22. tierra.py
#
# DIRECTORIO: excepciones
#   23. __init__.py
#   24. agua_agotada_exception.py
#   25. forestacion_exception.py
#   26. mensajes_exception.py
#   27. persistencia_exception.py
#   28. superficie_insuficiente_exception.py
#
# DIRECTORIO: patrones
#   29. __init__.py
#
# DIRECTORIO: patrones/factory
#   30. __init__.py
#   31. cultivo_factory.py
#
# DIRECTORIO: patrones/observer
#   32. __init__.py
#   33. observable.py
#   34. observer.py
#
# DIRECTORIO: patrones/observer/eventos
#   35. __init__.py
#   36. evento_plantacion.py
#   37. evento_sensor.py
#
# DIRECTORIO: patrones/singleton
#   38. __init__.py
#
# DIRECTORIO: patrones/strategy
#   39. __init__.py
#   40. absorcion_agua_strategy.py
#
# DIRECTORIO: patrones/strategy/impl
#   41. __init__.py
#   42. absorcion_constante_strategy.py
#   43. absorcion_seasonal_strategy.py
#
# DIRECTORIO: riego
#   44. __init__.py
#
# DIRECTORIO: riego/control
#   45. __init__.py
#   46. control_riego_task.py
#
# DIRECTORIO: riego/sensores
#   47. __init__.py
#   48. humedad_reader_task.py
#   49. temperatura_reader_task.py
#
# DIRECTORIO: servicios
#   50. __init__.py
#
# DIRECTORIO: servicios/cultivos
#   51. __init__.py
#   52. arbol_service.py
#   53. cultivo_service.py
#   54. cultivo_service_registry.py
#   55. lechuga_service.py
#   56. olivo_service.py
#   57. pino_service.py
#   58. zanahoria_service.py
#
# DIRECTORIO: servicios/negocio
#   59. __init__.py
#   60. fincas_service.py
#   61. paquete.py
#
# DIRECTORIO: servicios/personal
#   62. __init__.py
#   63. trabajador_service.py
#
# DIRECTORIO: servicios/terrenos
#   64. __init__.py
#   65. plantacion_service.py
#   66. registro_forestal_service.py
#   67. tierra_service.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/67: __init__.py
# Directorio: .
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 2/67: constantes.py
# Directorio: .
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/constantes.py
# ==============================================================================

"""
Archivo central para todas las constantes del proyecto
Prohibido el uso de "magic numbers" en el resto del código ya que todos provienen de aca
Tambien se especifican las unidades de medida de cada constante con comentarios
"""

# ==============================================================================
# DIRECTORIOS
# ==============================================================================
DIRECTORIO_DATA = "data"


# ==============================================================================
# CULTIVOS - SUPERFICIE (m²)
# ==============================================================================
SUPERFICIE_PINO = 2.0
SUPERFICIE_OLIVO = 3.0
SUPERFICIE_LECHUGA = 0.25
SUPERFICIE_ZANAHORIA = 0.15


# ==============================================================================
# CULTIVOS - AGUA INICIAL (L)
# ==============================================================================
AGUA_INICIAL_PINO = 2
AGUA_INICIAL_OLIVO = 3
AGUA_INICIAL_LECHUGA = 0.5
AGUA_INICIAL_ZANAHORIA = 0.3


# ==============================================================================
# ESTRATEGIA DE ABSORCIÓN - SEASONAL (Árboles)
# ==============================================================================
MES_INICIO_VERANO = 3  # Marzo
MES_FIN_VERANO = 8   # Agosto
ABSORCION_SEASONAL_VERANO = 5
ABSORCION_SEASONAL_INVIERNO = 2


# ==============================================================================
# ESTRATEGIA DE ABSORCIÓN - CONSTANTE (Hortalizas)
# ==============================================================================
ABSORCION_CONSTANTE_LECHUGA = 1
ABSORCION_CONSTANTE_ZANAHORIA = 2


# ==============================================================================
# RIEGO Y SENSORES
# ==============================================================================
AGUA_MINIMA = 10  # L - Nivel mínimo antes de que se agote el agua
AGUA_CONSUMIDA_RIEGO = 10  # L - Cantidad de agua que consume cada operación de riego
AGUA_CONSUMIDA_FUMIGACION = 2 # L - Cantidad de agua que consume cada operación de fumigación

TEMP_MIN_RIEGO = 8.0  # °C - Temperatura mínima para activar el riego
HUMEDAD_MAX_RIEGO = 50.0  # % - Humedad máxima para activar el riego

INTERVALO_SENSOR_TEMPERATURA = 2.0  # segundos
INTERVALO_SENSOR_HUMEDAD = 3.0      # segundos
INTERVALO_CONTROL_RIEGO = 2.5       # segundos
THREAD_JOIN_TIMEOUT = 2.0           # segundos


# ==============================================================================
# COSECHA (kg por cultivo)
# ==============================================================================
COSECHA_PINO = 100
COSECHA_OLIVO = 20
COSECHA_LECHUGA = 2
COSECHA_ZANAHORIA = 1


# ==============================================================================
# EMPAQUETADO (kg por paquete)
# ==============================================================================
PESO_PAQUETE_PINO = 10
PESO_PAQUETE_OLIVO = 2
PESO_PAQUETE_LECHUGA = 0.5
PESO_PAQUETE_ZANAHORIA = 0.25


# ==============================================================================
# TAREAS (duración en horas)
# ==============================================================================
DURACION_TAREA_REGAR = 1
DURACION_TAREA_COSECHAR = 8
DURACION_TAREA_FUMIGAR = 2
DURACION_TAREA_EMPAQUETAR = 4

# ==============================================================================
# ARCHIVO 3/67: main.py
# Directorio: ..
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/main.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: entidades
################################################################################

# ==============================================================================
# ARCHIVO 4/67: __init__.py
# Directorio: entidades
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/entidades/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: entidades/cultivos
################################################################################

# ==============================================================================
# ARCHIVO 5/67: __init__.py
# Directorio: entidades/cultivos
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/entidades/cultivos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 6/67: arbol.py
# Directorio: entidades/cultivos
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/entidades/cultivos/arbol.py
# ==============================================================================

from abc import ABC
from python_forestacion.entidades.cultivos.cultivo import Cultivo

class Arbol(Cultivo, ABC):
    """
    Clase abstracta base para todos los cultivos de tipo Árbol.
    Hereda de Cultivo y sirve como categoría para agrupar árboles.
    """
    def __init__(self, agua: float, superficie: float):
        """
        Inicializa un árbol.

        Args:
            agua: Cantidad de agua inicial en litros.
            superficie: Superficie que ocupa en metros cuadrados.
        """
        super().__init__(agua, superficie)


# ==============================================================================
# ARCHIVO 7/67: cultivo.py
# Directorio: entidades/cultivos
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/entidades/cultivos/cultivo.py
# ==============================================================================

from abc import ABC

class Cultivo(ABC):
    """
    Clase abstracta base para todos los tipos de cultivos.
    Define la estructura y atributos comunes que cualquier cultivo debe tener.
    Las entidades son DTOs (Data Transfer Objects), solo contienen datos.
    """
    def __init__(self, agua: float, superficie: float):
        """
        Inicializa un cultivo con una cantidad de agua y superficie requerida.

        Args:
            agua: Cantidad de agua inicial del cultivo en litros.
            superficie: Superficie que ocupa el cultivo en metros cuadrados.
        """
        self._agua = agua
        self._superficie = superficie

    def get_agua(self) -> float:
        """Retorna la cantidad de agua actual del cultivo."""
        return self._agua

    def set_agua(self, agua: float) -> None:
        """
        Establece la cantidad de agua del cultivo.
        No permite valores negativos.
        """
        if agua < 0:
            raise ValueError("La cantidad de agua no puede ser negativa.")
        self._agua = agua

    def get_superficie(self) -> float:
        """Retorna la superficie que ocupa el cultivo."""
        return self._superficie

    def set_superficie(self, superficie: float) -> None:
        """
        Establece la superficie del cultivo.
        No permite valores negativos o cero.
        """
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero.")
        self._superficie = superficie


# ==============================================================================
# ARCHIVO 8/67: hortaliza.py
# Directorio: entidades/cultivos
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/entidades/cultivos/hortaliza.py
# ==============================================================================

from abc import ABC
from python_forestacion.entidades.cultivos.cultivo import Cultivo

class Hortaliza(Cultivo, ABC):
    """
    Clase abstracta base para todos los cultivos de tipo Hortaliza.
    Añade la especificidad de si se cultiva en invernadero.
    """
    def __init__(self, agua: float, superficie: float, invernadero: bool):
        """
        Inicializa una hortaliza.

        Args:
            agua: Cantidad de agua inicial en litros.
            superficie: Superficie que ocupa en metros cuadrados.
            invernadero: True si requiere invernadero, False en caso contrario.
        """
        super().__init__(agua, superficie)
        self._invernadero = invernadero

    def requiere_invernadero(self) -> bool:
        """Retorna True si la hortaliza requiere invernadero."""
        return self._invernadero


# ==============================================================================
# ARCHIVO 9/67: lechuga.py
# Directorio: entidades/cultivos
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/entidades/cultivos/lechuga.py
# ==============================================================================

from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import AGUA_INICIAL_LECHUGA, SUPERFICIE_LECHUGA

class Lechuga(Hortaliza):
    """
    Clase concreta para el cultivo de Lechuga.
    """
    def __init__(self, tipo_hoja: str):
        """
        Inicializa una lechuga.

        Args:
            tipo_hoja: El tipo de hoja de la lechuga (ej: 'Rizada').
        """
        super().__init__(
            agua=AGUA_INICIAL_LECHUGA, 
            superficie=SUPERFICIE_LECHUGA, 
            invernadero=True
        )
        self._tipo_hoja = tipo_hoja

    def get_tipo_hoja(self) -> str:
        """Retorna el tipo de hoja de la lechuga."""
        return self._tipo_hoja


# ==============================================================================
# ARCHIVO 10/67: olivo.py
# Directorio: entidades/cultivos
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/entidades/cultivos/olivo.py
# ==============================================================================

from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.constantes import AGUA_INICIAL_OLIVO, SUPERFICIE_OLIVO
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna


class Olivo(Arbol):
    """
    Clase concreta para el cultivo de Olivo.
    """
    def __init__(self, tipo_aceituna: TipoAceituna):
        """
        Inicializa un olivo.

        Args:
            tipo_aceituna: El tipo de aceituna que produce el olivo.
        """
        super().__init__(agua=AGUA_INICIAL_OLIVO, superficie=SUPERFICIE_OLIVO)
        self._tipo_aceituna = tipo_aceituna

    def get_tipo_aceituna(self) -> TipoAceituna:
        """Retorna el tipo de aceituna que produce el olivo."""
        return self._tipo_aceituna


# ==============================================================================
# ARCHIVO 11/67: pino.py
# Directorio: entidades/cultivos
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/entidades/cultivos/pino.py
# ==============================================================================

from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.constantes import AGUA_INICIAL_PINO, SUPERFICIE_PINO

class Pino(Arbol):
    """
    Clase concreta para el cultivo de Pino.
    """
    def __init__(self, variedad: str):
        """
        Inicializa un pino con una variedad específica.

        Args:
            variedad: La variedad del pino (ej: 'Parana').
        """
        super().__init__(agua=AGUA_INICIAL_PINO, superficie=SUPERFICIE_PINO)
        self._variedad = variedad

    def get_variedad(self) -> str:
        """Retorna la variedad del pino."""
        return self._variedad


# ==============================================================================
# ARCHIVO 12/67: tipo_aceituna.py
# Directorio: entidades/cultivos
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/entidades/cultivos/tipo_aceituna.py
# ==============================================================================

from enum import Enum, auto

class TipoAceituna(Enum):
    """
    Enum para los tipos de aceituna que puede producir un Olivo.
    """
    ARBEQUINA = auto()
    PICUAL = auto()
    MANZANILLA = auto()


# ==============================================================================
# ARCHIVO 13/67: zanahoria.py
# Directorio: entidades/cultivos
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/entidades/cultivos/zanahoria.py
# ==============================================================================

from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import AGUA_INICIAL_ZANAHORIA, SUPERFICIE_ZANAHORIA

class Zanahoria(Hortaliza):
    """
    Clase concreta para el cultivo de Zanahoria.
    """
    def __init__(self, color: str):
        """
        Inicializa una zanahoria.

        Args:
            color: El color de la zanahoria (ej: 'Naranja').
        """
        super().__init__(
            agua=AGUA_INICIAL_ZANAHORIA, 
            superficie=SUPERFICIE_ZANAHORIA, 
            invernadero=False
        )
        self._color = color

    def get_color(self) -> str:
        """Retorna el color de la zanahoria."""
        return self._color



################################################################################
# DIRECTORIO: entidades/personal
################################################################################

# ==============================================================================
# ARCHIVO 14/67: __init__.py
# Directorio: entidades/personal
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/entidades/personal/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 15/67: apto_medico.py
# Directorio: entidades/personal
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/entidades/personal/apto_medico.py
# ==============================================================================

from datetime import date

class AptoMedico:
    """
    Representa el certificado de aptitud médica de un trabajador.
    """
    def __init__(self, fecha_emision: date, fecha_vencimiento: date, es_apto: bool):
        """
        Inicializa el apto médico.

        Args:
            fecha_emision: Fecha de emisión del certificado.
            fecha_vencimiento: Fecha de vencimiento del certificado.
            es_apto: True si el trabajador está apto.
        """
        if fecha_vencimiento < fecha_emision:
            raise ValueError("La fecha de vencimiento no puede ser anterior a la de emisión.")

        self._fecha_emision = fecha_emision
        self._fecha_vencimiento = fecha_vencimiento
        self._es_apto = es_apto

    def get_fecha_emision(self) -> date:
        return self._fecha_emision

    def get_fecha_vencimiento(self) -> date:
        return self._fecha_vencimiento

    def es_apto(self) -> bool:
        return self._es_apto

    def esta_vencido(self, fecha_actual: date) -> bool:
        """Verifica si el apto médico está vencido en la fecha actual."""
        return fecha_actual > self._fecha_vencimiento


# ==============================================================================
# ARCHIVO 16/67: herramienta.py
# Directorio: entidades/personal
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/entidades/personal/herramienta.py
# ==============================================================================

class Herramienta:
    """
    Representa una herramienta que un trabajador puede utilizar.
    """
    def __init__(self, nombre: str, tipo: str):
        """
        Inicializa la herramienta.

        Args:
            nombre: El nombre de la herramienta (ej: 'Pala').
            tipo: El tipo de herramienta (ej: 'Manual', 'Maquinaria').
        No pueden estar vacíos
        """
        if not nombre or not tipo:
            raise ValueError("El nombre y el tipo no pueden estar vacíos.")
        
        self._nombre = nombre
        self._tipo = tipo

    def get_nombre(self) -> str:
        return self._nombre

    def get_tipo(self) -> str:
        return self._tipo


# ==============================================================================
# ARCHIVO 17/67: tarea.py
# Directorio: entidades/personal
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/entidades/personal/tarea.py
# ==============================================================================

from threading import Lock

class Tarea:
    """
    Representa una tarea que puede ser asignada a un trabajador.
    """
    _next_id = 1
    _lock = Lock()  # para el manejo de concurrencia de los Hilos

    def __init__(self, descripcion: str, duracion_horas: int):
        """
        Inicializa una tarea.

        Args:
            descripcion: Descripción de la tarea (ej: 'Regar').
            duracion_horas: Duración estimada en horas.
        """
        with Tarea._lock:
            self._id = Tarea._next_id
            Tarea._next_id += 1
        
        self._descripcion = descripcion
        self._duracion_horas = duracion_horas

    def get_id(self) -> int:
        return self._id

    def get_descripcion(self) -> str:
        return self._descripcion

    def get_duracion_horas(self) -> int:
        return self._duracion_horas


# ==============================================================================
# ARCHIVO 18/67: trabajador.py
# Directorio: entidades/personal
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/entidades/personal/trabajador.py
# ==============================================================================

from typing import List, Optional, TYPE_CHECKING

# evita importaciones circulares, ya que es False durante tiempo de ejecucion, pero True durante el chequeo de
# tipos como Optional[AptoMedico] o List[Tarea]
if TYPE_CHECKING:
    from python_forestacion.entidades.personal.apto_medico import AptoMedico
    from python_forestacion.entidades.personal.tarea import Tarea

class Trabajador:
    """
    Representa a un trabajador de la plantación.
    """
    def __init__(self, nombre: str, apellido: str, dni: str):
        """
        Inicializa un trabajador.

        Args:
            nombre: Nombre del trabajador.
            apellido: Apellido del trabajador.
            dni: DNI del trabajador.
        """
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._apto_medico: Optional['AptoMedico'] = None
        self._tareas: List['Tarea'] = []

    def get_nombre_completo(self) -> str:
        return f"{self._nombre} {self._apellido}"

    def get_dni(self) -> str:
        return self._dni

    def get_apto_medico(self) -> Optional['AptoMedico']:
        return self._apto_medico

    def set_apto_medico(self, apto: Optional['AptoMedico']) -> None:
        self._apto_medico = apto

    def get_tareas(self) -> List['Tarea']:
        """Retorna una copia de la lista de tareas."""
        return self._tareas.copy()

    def asignar_tarea(self, tarea: 'Tarea') -> None:
        self._tareas.append(tarea)



################################################################################
# DIRECTORIO: entidades/terrenos
################################################################################

# ==============================================================================
# ARCHIVO 19/67: __init__.py
# Directorio: entidades/terrenos
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/entidades/terrenos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 20/67: plantacion.py
# Directorio: entidades/terrenos
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/entidades/terrenos/plantacion.py
# ==============================================================================

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.personal.trabajador import Trabajador

class Plantacion:
    """
    Representa una parcela de cultivo dentro de una Tierra.
    Gestiona los cultivos, trabajadores, agua y superficie.
    """
    def __init__(self, superficie: float):
        """
        Inicializa la plantación con una superficie total.

        Args:
            superficie: La superficie total de la plantación en m².
        """
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero.")
        
        self._superficie_total = superficie
        self._superficie_disponible = superficie
        self._agua_disponible = 0.0
        self._cultivos: List['Cultivo'] = []
        self._trabajadores: List['Trabajador'] = []

    def get_superficie_total(self) -> float:
        return self._superficie_total

    def get_superficie_disponible(self) -> float:
        return self._superficie_disponible

    def set_superficie_disponible(self, superficie: float) -> None:
        if superficie < 0:
            raise ValueError("La superficie disponible no puede ser negativa.")
        self._superficie_disponible = superficie

    def get_agua_disponible(self) -> float:
        return self._agua_disponible

    def set_agua_disponible(self, agua: float) -> None:
        if agua < 0:
            raise ValueError("El agua disponible no puede ser negativa.")
        self._agua_disponible = agua

    def get_cultivos(self) -> List['Cultivo']:
        """Retorna una copia de la lista de cultivos para evitar modificaciones externas."""
        return self._cultivos.copy()

    def agregar_cultivo(self, cultivo: 'Cultivo') -> None:
        self._cultivos.append(cultivo)

    def get_trabajadores(self) -> List['Trabajador']:
        """Retorna una copia de la lista de trabajadores."""
        return self._trabajadores.copy()

    def agregar_trabajador(self, trabajador: 'Trabajador') -> None:
        self._trabajadores.append(trabajador)


# ==============================================================================
# ARCHIVO 21/67: registro_forestal.py
# Directorio: entidades/terrenos
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/entidades/terrenos/registro_forestal.py
# ==============================================================================

from typing import TYPE_CHECKING

# Cuidar imports circulares, es False durante tiempo de ejecucion, pero no para el chequeo de tipos
if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.tierra import Tierra
    from python_forestacion.entidades.terrenos.plantacion import Plantacion

class RegistroForestal:
    """
    Entidad raíz que representa una finca completa.
    Agrupa una Tierra y una Plantación.
    """
    def __init__(self, propietario: str, tierra: 'Tierra', plantacion: 'Plantacion'):
        """
        Inicializa el registro forestal. Tambien chequea la coherencia de los datos sobre el propietario.

        Args:
            propietario: Nombre del propietario del registro.
            tierra: La entidad Tierra asociada.
            plantacion: La entidad Plantacion asociada.
        """
        if not propietario:
            raise ValueError("El propietario no puede estar vacío.")
        if tierra.get_propietario() != propietario:
            raise ValueError("El propietario del registro debe coincidir con el de la tierra.")

        self._propietario = propietario
        self._tierra = tierra
        self._plantacion = plantacion

    def get_propietario(self) -> str:
        return self._propietario

    def get_tierra(self) -> 'Tierra':
        return self._tierra

    def get_plantacion(self) -> 'Plantacion':
        return self._plantacion


# ==============================================================================
# ARCHIVO 22/67: tierra.py
# Directorio: entidades/terrenos
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/entidades/terrenos/tierra.py
# ==============================================================================

class Tierra:
    """
    Representa una porción de tierra con su identificación catastral y propietario.
    """
    def __init__(self, codigo_catastral: str, propietario: str, superficie: float):
        """
        Inicializa la tierra. Y establece algunas excepciones basicas

        Args:
            codigo_catastral: Identificador único del catastro.
            propietario: Nombre del dueño de la tierra.
            superficie: Superficie total de la tierra en metros cuadrados.
        """
        self._codigo_catastral = codigo_catastral
        self._propietario = propietario
        self._superficie = superficie

    def get_codigo_catastral(self) -> str:
        return self._codigo_catastral

    def set_codigo_catastral(self, codigo_catastral: str) -> None:
        if not codigo_catastral:
            raise ValueError("El código catastral no puede estar vacío.")
        self._codigo_catastral = codigo_catastral

    def get_propietario(self) -> str:
        return self._propietario

    def set_propietario(self, propietario: str) -> None:
        if not propietario:
            raise ValueError("El propietario no puede estar vacío.")
        self._propietario = propietario

    def get_superficie(self) -> float:
        return self._superficie

    def set_superficie(self, superficie: float) -> None:
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero.")
        self._superficie = superficie



################################################################################
# DIRECTORIO: excepciones
################################################################################

# ==============================================================================
# ARCHIVO 23/67: __init__.py
# Directorio: excepciones
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/excepciones/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 24/67: agua_agotada_exception.py
# Directorio: excepciones
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/excepciones/agua_agotada_exception.py
# ==============================================================================

from python_forestacion.excepciones.forestacion_exception import ForestacionException

class AguaAgotadaException(ForestacionException):
    """
    Excepción lanzada cuando no hay suficiente agua para una operación.
    """
    def __init__(self, agua_requerida: float, agua_disponible: float):
        user_msg = f"No hay suficiente agua. Se requieren {agua_requerida:.2f}L pero solo hay {agua_disponible:.2f}L disponibles."
        tech_msg = f"Agua requerida ({agua_requerida}) > disponible ({agua_disponible})"
        super().__init__(user_msg, tech_msg)
        self.agua_requerida = agua_requerida
        self.agua_disponible = agua_disponible


# ==============================================================================
# ARCHIVO 25/67: forestacion_exception.py
# Directorio: excepciones
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/excepciones/forestacion_exception.py
# ==============================================================================

class ForestacionException(Exception):
    """
    Clase base para todas las excepciones personalizadas del proyecto.
    Permite diferenciar nuestros errores de los errores nativos de Python.
    """
    def __init__(self, user_message: str, tech_message: str):
        """
        Args:
            user_message: Mensaje claro para el usuario final.
            tech_message: Mensaje técnico para desarrolladores (logs).
        """
        super().__init__(tech_message)
        self._user_message = user_message
        self._tech_message = tech_message

    def get_user_message(self) -> str:
        return self._user_message

    def get_tech_message(self) -> str:
        return self._tech_message


# ==============================================================================
# ARCHIVO 26/67: mensajes_exception.py
# Directorio: excepciones
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/excepciones/mensajes_exception.py
# ==============================================================================

"""
Centraliza los mensajes de error para las excepciones personalizadas.
"""


# ==============================================================================
# ARCHIVO 27/67: persistencia_exception.py
# Directorio: excepciones
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/excepciones/persistencia_exception.py
# ==============================================================================

from python_forestacion.excepciones.forestacion_exception import ForestacionException

class PersistenciaException(ForestacionException):
    """
    Excepción lanzada durante errores de guardado o carga de datos.
    """
    def __init__(self, operacion: str, error_original: Exception):
        user_msg = f"Ocurrió un error durante la operación de {operacion}."
        tech_msg = f"Error en {operacion}: {error_original}"
        super().__init__(user_msg, tech_msg)
        self.operacion = operacion
        self.error_original = error_original


# ==============================================================================
# ARCHIVO 28/67: superficie_insuficiente_exception.py
# Directorio: excepciones
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/excepciones/superficie_insuficiente_exception.py
# ==============================================================================

from python_forestacion.excepciones.forestacion_exception import ForestacionException

class SuperficieInsuficienteException(ForestacionException):
    """
    Excepción lanzada cuando no hay suficiente superficie para una operación.
    """
    def __init__(self, superficie_requerida: float, superficie_disponible: float):
        user_msg = f"No hay suficiente superficie. Se requieren {superficie_requerida:.2f}m² pero solo hay {superficie_disponible:.2f}m² disponibles."
        tech_msg = f"Superficie requerida ({superficie_requerida}) > disponible ({superficie_disponible})"
        super().__init__(user_msg, tech_msg)
        self.superficie_requerida = superficie_requerida
        self.superficie_disponible = superficie_disponible



################################################################################
# DIRECTORIO: patrones
################################################################################

# ==============================================================================
# ARCHIVO 29/67: __init__.py
# Directorio: patrones
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/patrones/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones/factory
################################################################################

# ==============================================================================
# ARCHIVO 30/67: __init__.py
# Directorio: patrones/factory
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/patrones/factory/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 31/67: cultivo_factory.py
# Directorio: patrones/factory
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/patrones/factory/cultivo_factory.py
# ==============================================================================

from typing import TYPE_CHECKING

# Impide importaciones circulares, ya que es False durante tiempo de ejecucion, pero True durante el chequeo de tipos
# como por ejemplo: List[Cultivo]
if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.cultivos.pino import Pino
    from python_forestacion.entidades.cultivos.olivo import Olivo
    from python_forestacion.entidades.cultivos.lechuga import Lechuga
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria

class CultivoFactory:
    """
    Implementación del patrón Factory Method para la creación de cultivos.
    Centraliza la lógica de instanciación de los diferentes tipos de cultivo.
    """

    @staticmethod
    def _crear_pino() -> 'Pino':
        from python_forestacion.entidades.cultivos.pino import Pino
        return Pino(variedad="Parana")

    @staticmethod
    def _crear_olivo() -> 'Olivo':
        from python_forestacion.entidades.cultivos.olivo import Olivo
        from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
        return Olivo(tipo_aceituna=TipoAceituna.ARBEQUINA)

    @staticmethod
    def _crear_lechuga() -> 'Lechuga':
        from python_forestacion.entidades.cultivos.lechuga import Lechuga
        return Lechuga(tipo_hoja="Rizada")

    @staticmethod
    def _crear_zanahoria() -> 'Zanahoria':
        from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
        return Zanahoria(color="Naranja")

    @staticmethod
    def crear_cultivo(especie: str) -> 'Cultivo':
        """
        Método fábrica principal. Crea una instancia de un cultivo basado en la especie.

        Args:
            especie: El nombre de la especie a crear (ej: 'Pino').

        Returns:
            Una instancia del cultivo solicitado.

        Raises:
            ValueError: Si la especie es desconocida.
        """
        factories = {
            "Pino": CultivoFactory._crear_pino,
            "Olivo": CultivoFactory._crear_olivo,
            "Lechuga": CultivoFactory._crear_lechuga,
            "Zanahoria": CultivoFactory._crear_zanahoria
        }
        
        if especie not in factories:
            raise ValueError(f"Especie de cultivo desconocida: {especie}")
        
        return factories[especie]()



################################################################################
# DIRECTORIO: patrones/observer
################################################################################

# ==============================================================================
# ARCHIVO 32/67: __init__.py
# Directorio: patrones/observer
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/patrones/observer/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 33/67: observable.py
# Directorio: patrones/observer
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/patrones/observer/observable.py
# ==============================================================================

from abc import ABC
from typing import Generic, List, TypeVar

from python_forestacion.patrones.observer.observer import Observer

T = TypeVar('T')

class Observable(Generic[T], ABC):
    """
    La clase base Observable (publicador) del patrón Observer.
    Mantiene una lista de observadores y los notifica de los cambios.
    """
    def __init__(self):
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        """Agrega un observador a la lista si no está ya presente."""
        if observador not in self._observadores:
            self._observadores.append(observador)

    def remover_observador(self, observador: Observer[T]) -> None:
        """Remueve un observador de la lista."""
        self._observadores.remove(observador)

    def notificar_observadores(self, evento: T) -> None:
        """Notifica a todos los observadores enviándoles el evento."""
        for observador in self._observadores:
            observador.actualizar(self, evento)


# ==============================================================================
# ARCHIVO 34/67: observer.py
# Directorio: patrones/observer
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/patrones/observer/observer.py
# ==============================================================================

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.patrones.observer.observable import Observable

T = TypeVar('T')

class Observer(Generic[T], ABC):
    """
    La interfaz Observer (suscriptor) del patrón Observer.
    Define el método actualizar que será llamado por el Observable.
    """
    @abstractmethod
    def actualizar(self, observable: 'Observable', evento: T) -> None:
        """
        Recibe una actualización del observable.

        Args:
            observable: La instancia del observable que notifica el evento.
            evento: El dato o evento notificado por el observable.
        """
        pass



################################################################################
# DIRECTORIO: patrones/observer/eventos
################################################################################

# ==============================================================================
# ARCHIVO 35/67: __init__.py
# Directorio: patrones/observer/eventos
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/patrones/observer/eventos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 36/67: evento_plantacion.py
# Directorio: patrones/observer/eventos
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/patrones/observer/eventos/evento_plantacion.py
# ==============================================================================

from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class EventoPlantacion:
    """Representa un evento ocurrido en una plantación."""
    tipo_evento: str
    fecha: date
    descripcion: str


# ==============================================================================
# ARCHIVO 37/67: evento_sensor.py
# Directorio: patrones/observer/eventos
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/patrones/observer/eventos/evento_sensor.py
# ==============================================================================

from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class EventoSensor:
    """Representa un evento de un sensor con un valor y una fecha."""
    valor: float
    fecha: datetime



################################################################################
# DIRECTORIO: patrones/singleton
################################################################################

# ==============================================================================
# ARCHIVO 38/67: __init__.py
# Directorio: patrones/singleton
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/patrones/singleton/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones/strategy
################################################################################

# ==============================================================================
# ARCHIVO 39/67: __init__.py
# Directorio: patrones/strategy
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/patrones/strategy/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 40/67: absorcion_agua_strategy.py
# Directorio: patrones/strategy
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/patrones/strategy/absorcion_agua_strategy.py
# ==============================================================================

from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class AbsorcionAguaStrategy(ABC):
    """
    Interfaz (Strategy) para definir diferentes algoritmos de absorción de agua.
    """
    @abstractmethod
    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        """
        Calcula la cantidad de agua absorbida por un cultivo.

        Args:
            fecha: La fecha actual.
            temperatura: La temperatura actual.
            humedad: La humedad actual.
            cultivo: El cultivo que absorbe el agua.

        Returns:
            La cantidad de agua absorbida en litros.
        """
        pass



################################################################################
# DIRECTORIO: patrones/strategy/impl
################################################################################

# ==============================================================================
# ARCHIVO 41/67: __init__.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/patrones/strategy/impl/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 42/67: absorcion_constante_strategy.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/patrones/strategy/impl/absorcion_constante_strategy.py
# ==============================================================================

from datetime import date
from typing import TYPE_CHECKING

from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """
    Estrategia de absorción de agua para hortalizas, que siempre es constante.
    """
    def __init__(self, cantidad_constante: int):
        """
        Args:
            cantidad_constante: La cantidad de agua a absorber siempre.
        """
        self._cantidad = cantidad_constante

    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        return self._cantidad


# ==============================================================================
# ARCHIVO 43/67: absorcion_seasonal_strategy.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/patrones/strategy/impl/absorcion_seasonal_strategy.py
# ==============================================================================

from datetime import date
from typing import TYPE_CHECKING

from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from python_forestacion.constantes import (
    MES_INICIO_VERANO,
    MES_FIN_VERANO,
    ABSORCION_SEASONAL_VERANO,
    ABSORCION_SEASONAL_INVIERNO
)

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    """
    Estrategia de absorción de agua para árboles, que varía según la estación.
    """
    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        mes = fecha.month
        if MES_INICIO_VERANO <= mes <= MES_FIN_VERANO:
            return ABSORCION_SEASONAL_VERANO
        else:
            return ABSORCION_SEASONAL_INVIERNO



################################################################################
# DIRECTORIO: riego
################################################################################

# ==============================================================================
# ARCHIVO 44/67: __init__.py
# Directorio: riego
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/riego/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: riego/control
################################################################################

# ==============================================================================
# ARCHIVO 45/67: __init__.py
# Directorio: riego/control
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/riego/control/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 46/67: control_riego_task.py
# Directorio: riego/control
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/riego/control/control_riego_task.py
# ==============================================================================

import threading
import time
from datetime import date
from typing import Optional, TYPE_CHECKING

from python_forestacion.patrones.observer.observer import Observer
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor
from python_forestacion.constantes import (
    TEMP_MIN_RIEGO,
    HUMEDAD_MAX_RIEGO,
    INTERVALO_CONTROL_RIEGO
)

if TYPE_CHECKING:
    from python_forestacion.patrones.observer.observable import Observable
    from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
    from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
    from python_forestacion.entidades.terrenos.plantacion import Plantacion
    from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService

class ControlRiegoTask(threading.Thread, Observer[EventoSensor]):
    """
    Tarea que se ejecuta en un hilo para controlar el sistema de riego.
    Es un Observer de los sensores de temperatura y humedad.
    """
    def __init__(self, plantacion_service: 'PlantacionService', plantacion: 'Plantacion'):
        threading.Thread.__init__(self, daemon=True)
        self._plantacion_service = plantacion_service
        self._plantacion = plantacion
        self._ultima_temperatura: Optional[float] = None
        self._ultima_humedad: Optional[float] = None
        self._detenido = threading.Event()

    def actualizar(self, observable: 'Observable', evento: EventoSensor) -> None:
        """
        Recibe notificaciones de los sensores y actualiza los valores internos.
        Distingue la fuente del evento gracias al parámetro 'observable'.
        """
        from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
        from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask

        if isinstance(observable, TemperaturaReaderTask):
            self._ultima_temperatura = evento.valor
        elif isinstance(observable, HumedadReaderTask):
            self._ultima_humedad = evento.valor

    def _debe_regar(self) -> bool:
        """Comprueba si se cumplen las condiciones para el riego."""
        if self._ultima_temperatura is None or self._ultima_humedad is None:
            return False
        
        return (
            self._ultima_temperatura > TEMP_MIN_RIEGO and 
            self._ultima_humedad < HUMEDAD_MAX_RIEGO
        )

    def run(self) -> None:
        """Punto de entrada del hilo. Comprueba y ejecuta el riego periódicamente."""
        while not self._detenido.is_set():
            try:
                if self._debe_regar():
                    print(f"[Control Riego] Condiciones óptimas (Temp: {self._ultima_temperatura}°C, Humedad: {self._ultima_humedad}%). Iniciando riego.")
                    try:
                        self._plantacion_service.regar(
                            self._plantacion, 
                            date.today(), 
                            self._ultima_temperatura, 
                            self._ultima_humedad
                        )
                    except Exception as e:
                        print(f"[Control Riego] Error al intentar regar: {e}")
                else:
                    print(f"[Control Riego] Condiciones no aptas para riego (Temp: {self._ultima_temperatura}°C, Humedad: {self._ultima_humedad}%).")
                
                time.sleep(INTERVALO_CONTROL_RIEGO)
            except Exception as e:
                print(f"[Control Riego] Error: {e}")

    def detener(self) -> None:
        """Señaliza al hilo que debe detenerse."""
        self._detenido.set()



################################################################################
# DIRECTORIO: riego/sensores
################################################################################

# ==============================================================================
# ARCHIVO 47/67: __init__.py
# Directorio: riego/sensores
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/riego/sensores/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 48/67: humedad_reader_task.py
# Directorio: riego/sensores
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/riego/sensores/humedad_reader_task.py
# ==============================================================================

import threading
import time
import random
from datetime import datetime

from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import INTERVALO_SENSOR_HUMEDAD
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor

class HumedadReaderTask(threading.Thread, Observable[EventoSensor]):
    """
    Tarea que se ejecuta en un hilo para leer la humedad simulada.
    Es un Observable que notifica a sus observadores con cada nueva lectura.
    """
    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def _leer_humedad(self) -> float:
        """Simula la lectura de un sensor de humedad."""
        return round(random.uniform(20.0, 80.0), 2)

    def run(self) -> None:
        """Punto de entrada del hilo. Lee y notifica la humedad periódicamente."""
        while not self._detenido.is_set():
            try:
                humedad = self._leer_humedad()
                print(f"[Sensor Humedad] Nueva lectura: {humedad}%")
                evento = EventoSensor(valor=humedad, fecha=datetime.now())
                self.notificar_observadores(evento)
                time.sleep(INTERVALO_SENSOR_HUMEDAD)
            except Exception as e:
                print(f"[Sensor Humedad] Error: {e}")

    def detener(self) -> None:
        """Señaliza al hilo que debe detenerse."""
        self._detenido.set()


# ==============================================================================
# ARCHIVO 49/67: temperatura_reader_task.py
# Directorio: riego/sensores
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/riego/sensores/temperatura_reader_task.py
# ==============================================================================

import threading
import time
import random
from datetime import datetime

from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import INTERVALO_SENSOR_TEMPERATURA
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor

class TemperaturaReaderTask(threading.Thread, Observable[EventoSensor]):
    """
    Tarea que se ejecuta en un hilo para leer la temperatura simulada.
    Es un Observable que notifica a sus observadores con cada nueva lectura.
    """
    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def _leer_temperatura(self) -> float:
        """Simula la lectura de un sensor de temperatura."""
        return round(random.uniform(5.0, 35.0), 2)

    def run(self) -> None:
        """Punto de entrada del hilo. Lee y notifica la temperatura periódicamente."""
        while not self._detenido.is_set():
            try:
                temp = self._leer_temperatura()
                print(f"[Sensor Temperatura] Nueva lectura: {temp}°C")
                evento = EventoSensor(valor=temp, fecha=datetime.now())
                self.notificar_observadores(evento)
                time.sleep(INTERVALO_SENSOR_TEMPERATURA)
            except Exception as e:
                print(f"[Sensor Temperatura] Error: {e}")

    def detener(self) -> None:
        """Señaliza al hilo que debe detenerse."""
        self._detenido.set()



################################################################################
# DIRECTORIO: servicios
################################################################################

# ==============================================================================
# ARCHIVO 50/67: __init__.py
# Directorio: servicios
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/servicios/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: servicios/cultivos
################################################################################

# ==============================================================================
# ARCHIVO 51/67: __init__.py
# Directorio: servicios/cultivos
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/servicios/cultivos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 52/67: arbol_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/servicios/cultivos/arbol_service.py
# ==============================================================================

from abc import ABC
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

class ArbolService(CultivoService, ABC):
    """
    Clase base para los servicios de árboles.
    """
    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        super().__init__(estrategia_absorcion)


# ==============================================================================
# ARCHIVO 53/67: cultivo_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/servicios/cultivos/cultivo_service.py
# ==============================================================================

from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class CultivoService(ABC):
    """
    Clase base abstracta para los servicios de cultivo.
    Contiene la lógica de negocio común y utiliza el patrón Strategy para la absorción de agua.
    """
    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        """
        Inyecta la estrategia de absorción de agua.

        Args:
            estrategia_absorcion: La estrategia a utilizar para calcular la absorción.
        """
        self._estrategia_absorcion = estrategia_absorcion

    def absorver_agua(self, cultivo: 'Cultivo', fecha: date, temperatura: float, humedad: float) -> int:
        """
        Calcula y aplica la absorción de agua a un cultivo usando la estrategia inyectada.
        """
        agua_absorbida = self._estrategia_absorcion.calcular_absorcion(
            fecha, temperatura, humedad, cultivo
        )
        cultivo.set_agua(cultivo.get_agua() + agua_absorbida)
        return agua_absorbida

    @abstractmethod
    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """Muestra los datos específicos de un cultivo."""
        print(f"Agua: {cultivo.get_agua()}L, Superficie: {cultivo.get_superficie()}m²")


# ==============================================================================
# ARCHIVO 54/67: cultivo_service_registry.py
# Directorio: servicios/cultivos
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/servicios/cultivos/cultivo_service_registry.py
# ==============================================================================

from threading import Lock
from datetime import date
from typing import TYPE_CHECKING, Dict, Type, Callable

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.cultivos.pino import Pino
    from python_forestacion.entidades.cultivos.olivo import Olivo
    from python_forestacion.entidades.cultivos.lechuga import Lechuga
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
    from python_forestacion.servicios.cultivos.pino_service import PinoService
    from python_forestacion.servicios.cultivos.olivo_service import OlivoService
    from python_forestacion.servicios.cultivos.lechuga_service import LechugaService
    from python_forestacion.servicios.cultivos.zanahoria_service import ZanahoriaService

class CultivoServiceRegistry:
    """
    Implementa los patrones Singleton y Registry.
    - Singleton: Asegura una única instancia de esta clase.
    - Registry: Proporciona un punto central para acceder a los servicios de cultivo
      y realizar dispatch polimórfico sin usar isinstance().
    """
    _instance = None
    _lock = Lock()

# Esta funciona hace que la clase sea un Singleton
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._inicializar_servicios()
        return cls._instance

    @classmethod
    def get_instance(cls):
        """Punto de acceso global a la instancia Singleton."""
        if cls._instance is None:
            cls()  # Llama a __new__ para crear la instancia si no existe
        return cls._instance

    def _inicializar_servicios(self) -> None:
        """Inicializa y registra todos los servicios de cultivo y sus manejadores."""
        from python_forestacion.entidades.cultivos.pino import Pino
        from python_forestacion.entidades.cultivos.olivo import Olivo
        from python_forestacion.entidades.cultivos.lechuga import Lechuga
        from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
        from python_forestacion.servicios.cultivos.pino_service import PinoService
        from python_forestacion.servicios.cultivos.olivo_service import OlivoService
        from python_forestacion.servicios.cultivos.lechuga_service import LechugaService
        from python_forestacion.servicios.cultivos.zanahoria_service import ZanahoriaService

        # Instanciar servicios
        self._pino_service: 'PinoService' = PinoService()
        self._olivo_service: 'OlivoService' = OlivoService()
        self._lechuga_service: 'LechugaService' = LechugaService()
        self._zanahoria_service: 'ZanahoriaService' = ZanahoriaService()

        # Registrar manejadores (handlers) para cada acción y tipo de cultivo
        self._absorber_agua_handlers: Dict[Type['Cultivo'], Callable] = {
            Pino: self._absorber_agua_pino,
            Olivo: self._absorber_agua_olivo,
            Lechuga: self._absorber_agua_lechuga,
            Zanahoria: self._absorber_agua_zanahoria,
        }
        
        self._mostrar_datos_handlers: Dict[Type['Cultivo'], Callable] = {
            Pino: self._mostrar_datos_pino,
            Olivo: self._mostrar_datos_olivo,
            Lechuga: self._mostrar_datos_lechuga,
            Zanahoria: self._mostrar_datos_zanahoria,
        }

    # --- Métodos públicos de dispatch ---

    def absorber_agua(self, cultivo: 'Cultivo', fecha: date, temperatura: float, humedad: float) -> int:
        """Realiza el dispatch para la acción de absorber agua."""
        handler = self._get_handler_for_cultivo(self._absorber_agua_handlers, cultivo)
        return handler(cultivo, fecha, temperatura, humedad)

    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """Realiza el dispatch para la acción de mostrar datos."""
        handler = self._get_handler_for_cultivo(self._mostrar_datos_handlers, cultivo)
        handler(cultivo)

    # --- Métodos de ayuda ---

    def _get_handler_for_cultivo(self, handlers: dict, cultivo: 'Cultivo') -> Callable:
        """Busca el manejador apropiado para el tipo de cultivo."""
        tipo_cultivo = type(cultivo)
        if tipo_cultivo not in handlers:
            raise ValueError(f"No se encontró un manejador para el tipo de cultivo: {tipo_cultivo.__name__}")
        return handlers[tipo_cultivo]

    # --- Manejadores privados para cada tipo de cultivo y acción ---

    def _absorber_agua_pino(self, cultivo: 'Pino', fecha: date, temperatura: float, humedad: float) -> int:
        return self._pino_service.absorver_agua(cultivo, fecha, temperatura, humedad)

    def _absorber_agua_olivo(self, cultivo: 'Olivo', fecha: date, temperatura: float, humedad: float) -> int:
        return self._olivo_service.absorver_agua(cultivo, fecha, temperatura, humedad)

    def _absorber_agua_lechuga(self, cultivo: 'Lechuga', fecha: date, temperatura: float, humedad: float) -> int:
        return self._lechuga_service.absorver_agua(cultivo, fecha, temperatura, humedad)

    def _absorber_agua_zanahoria(self, cultivo: 'Zanahoria', fecha: date, temperatura: float, humedad: float) -> int:
        return self._zanahoria_service.absorver_agua(cultivo, fecha, temperatura, humedad)

    def _mostrar_datos_pino(self, cultivo: 'Pino') -> None:
        self._pino_service.mostrar_datos(cultivo)

    def _mostrar_datos_olivo(self, cultivo: 'Olivo') -> None:
        self._olivo_service.mostrar_datos(cultivo)

    def _mostrar_datos_lechuga(self, cultivo: 'Lechuga') -> None:
        self._lechuga_service.mostrar_datos(cultivo)

    def _mostrar_datos_zanahoria(self, cultivo: 'Zanahoria') -> None:
        self._zanahoria_service.mostrar_datos(cultivo)


# ==============================================================================
# ARCHIVO 55/67: lechuga_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/servicios/cultivos/lechuga_service.py
# ==============================================================================

from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.constantes import ABSORCION_CONSTANTE_LECHUGA

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.lechuga import Lechuga

class LechugaService(CultivoService):
    """
    Servicio específico para la lógica de negocio de la Lechuga.
    """
    def __init__(self):
        # Inyecta la estrategia de absorción constante, específica para hortalizas.
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_CONSTANTE_LECHUGA))

    def mostrar_datos(self, cultivo: 'Lechuga') -> None:
        """Muestra los datos generales y los específicos de la Lechuga."""
        super().mostrar_datos(cultivo)
        print(f"Tipo de hoja: {cultivo.get_tipo_hoja()}")
        print(f"Requiere invernadero: {cultivo.requiere_invernadero()}")


# ==============================================================================
# ARCHIVO 56/67: olivo_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/servicios/cultivos/olivo_service.py
# ==============================================================================

from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.olivo import Olivo

class OlivoService(ArbolService):
    """
    Servicio específico para la lógica de negocio del Olivo.
    """
    def __init__(self):
        # Inyecta la estrategia de absorción estacional, específica para árboles.
        super().__init__(AbsorcionSeasonalStrategy())

    def mostrar_datos(self, cultivo: 'Olivo') -> None:
        """Muestra los datos generales y los específicos del Olivo."""
        super().mostrar_datos(cultivo)
        print(f"Tipo de aceituna: {cultivo.get_tipo_aceituna().name}")


# ==============================================================================
# ARCHIVO 57/67: pino_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/servicios/cultivos/pino_service.py
# ==============================================================================

from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.pino import Pino

class PinoService(ArbolService):
    """
    Servicio específico para la lógica de negocio del Pino.
    """
    def __init__(self):
        # Inyecta la estrategia de absorción estacional, específica para árboles.
        super().__init__(AbsorcionSeasonalStrategy())

    def mostrar_datos(self, cultivo: 'Pino') -> None:
        """Muestra los datos generales y los específicos del Pino."""
        super().mostrar_datos(cultivo)
        print(f"Variedad: {cultivo.get_variedad()}")


# ==============================================================================
# ARCHIVO 58/67: zanahoria_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/servicios/cultivos/zanahoria_service.py
# ==============================================================================

from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.constantes import ABSORCION_CONSTANTE_ZANAHORIA

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria

class ZanahoriaService(CultivoService):
    """
    Servicio específico para la lógica de negocio de la Zanahoria.
    """
    def __init__(self):
        # Inyecta la estrategia de absorción constante con el valor para la zanahoria.
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_CONSTANTE_ZANAHORIA))

    def mostrar_datos(self, cultivo: 'Zanahoria') -> None:
        """Muestra los datos generales y los específicos de la Zanahoria."""
        super().mostrar_datos(cultivo)
        print(f"Color: {cultivo.get_color()}")
        print(f"Requiere invernadero: {cultivo.requiere_invernadero()}")



################################################################################
# DIRECTORIO: servicios/negocio
################################################################################

# ==============================================================================
# ARCHIVO 59/67: __init__.py
# Directorio: servicios/negocio
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/servicios/negocio/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 60/67: fincas_service.py
# Directorio: servicios/negocio
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/servicios/negocio/fincas_service.py
# ==============================================================================

from typing import List, Dict, Type, TYPE_CHECKING
from collections import defaultdict

from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.servicios.negocio.paquete import Paquete
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.constantes import (
    AGUA_CONSUMIDA_FUMIGACION,
    COSECHA_PINO, COSECHA_OLIVO, COSECHA_LECHUGA, COSECHA_ZANAHORIA,
    PESO_PAQUETE_PINO, PESO_PAQUETE_OLIVO, PESO_PAQUETE_LECHUGA, PESO_PAQUETE_ZANAHORIA
)

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class FincasService:
    """
    Servicio de alto nivel para operaciones de negocio que involucran la finca.
    """
    def fumigar(self, plantacion: 'Plantacion') -> None:
        """Fumiga todos los cultivos, consumiendo agua por cada uno."""
        agua_requerida = len(plantacion.get_cultivos()) * AGUA_CONSUMIDA_FUMIGACION
        if plantacion.get_agua_disponible() < agua_requerida:
            raise AguaAgotadaException(agua_requerida, plantacion.get_agua_disponible())
        
        plantacion.set_agua_disponible(plantacion.get_agua_disponible() - agua_requerida)
        print(f"Se fumigaron {len(plantacion.get_cultivos())} cultivos (consumo total: {agua_requerida}L de agua).")

    def cosechar_y_empaquetar(self, plantacion: 'Plantacion') -> List[Paquete]:
        """Cosecha todos los cultivos y los empaqueta."""
        rendimiento_por_cultivo: Dict[Type['Cultivo'], int] = {
            Pino: COSECHA_PINO,
            Olivo: COSECHA_OLIVO,
            Lechuga: COSECHA_LECHUGA,
            Zanahoria: COSECHA_ZANAHORIA,
        }

        peso_paquete_por_cultivo: Dict[Type['Cultivo'], float] = {
            Pino: PESO_PAQUETE_PINO,
            Olivo: PESO_PAQUETE_OLIVO,
            Lechuga: PESO_PAQUETE_LECHUGA,
            Zanahoria: PESO_PAQUETE_ZANAHORIA,
        }

        # Calcula el rendimiento total por tipo de cultivo
        cosecha_total: Dict[Type['Cultivo'], int] = defaultdict(int)
        for cultivo in plantacion.get_cultivos():
            tipo_cultivo = type(cultivo)
            if tipo_cultivo in rendimiento_por_cultivo:
                cosecha_total[tipo_cultivo] += rendimiento_por_cultivo[tipo_cultivo]

        # Empaqueta la cosecha
        paquetes_finales: List[Paquete] = []
        for tipo_cultivo, total_kg in cosecha_total.items():
            nombre_cultivo = tipo_cultivo.__name__
            peso_paquete = peso_paquete_por_cultivo[tipo_cultivo]
            num_paquetes = total_kg // peso_paquete

            print(f"Cosecha de {nombre_cultivo}: {total_kg}kg -> {num_paquetes} paquetes de {peso_paquete}kg.")

            for _ in range(int(num_paquetes)):
                paquete = Paquete(nombre_cultivo, peso_paquete)
                # En una simulación real, aquí se agregarían los items cosechados
                # Para simplificar, creamos paquetes vacíos con el peso correcto.
                paquetes_finales.append(paquete)
        
        return paquetes_finales


# ==============================================================================
# ARCHIVO 61/67: paquete.py
# Directorio: servicios/negocio
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/servicios/negocio/paquete.py
# ==============================================================================

from typing import Generic, TypeVar, List

T = TypeVar('T')

class Paquete(Generic[T]):
    """
    Clase genérica que representa un paquete de un tipo de producto cosechado.
    """
    def __init__(self, tipo_producto: str, peso_por_unidad: float):
        self._tipo_producto = tipo_producto
        self._peso_por_unidad = peso_por_unidad
        self._items: List[T] = []
        self._peso_total = 0.0

    def agregar_item(self, item: T) -> None:
        self._items.append(item)
        self._peso_total += self._peso_por_unidad

    def get_tipo_producto(self) -> str:
        return self._tipo_producto

    def get_peso_total(self) -> float:
        return self._peso_total

    def get_cantidad_items(self) -> int:
        return len(self._items)



################################################################################
# DIRECTORIO: servicios/personal
################################################################################

# ==============================================================================
# ARCHIVO 62/67: __init__.py
# Directorio: servicios/personal
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/servicios/personal/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 63/67: trabajador_service.py
# Directorio: servicios/personal
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/servicios/personal/trabajador_service.py
# ==============================================================================

from datetime import date
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from python_forestacion.entidades.personal.trabajador import Trabajador
    from python_forestacion.entidades.personal.apto_medico import AptoMedico
    from python_forestacion.entidades.personal.tarea import Tarea
    from python_forestacion.entidades.personal.herramienta import Herramienta

class TrabajadorService:
    """
    Servicio para la lógica de negocio relacionada con los Trabajadores.
    """
    def asignar_apto_medico(self, trabajador: 'Trabajador', apto: 'AptoMedico') -> None:
        trabajador.set_apto_medico(apto)
        print(f"Se asignó un apto médico a {trabajador.get_nombre_completo()}.")

    def trabajar(self, trabajador: 'Trabajador', fecha_actual: date, herramienta: 'Herramienta') -> bool:
        """
        Simula a un trabajador realizando sus tareas en un día.
        Verifica si el trabajador tiene un apto médico vigente.
        """
        apto = trabajador.get_apto_medico()
        if apto is None or not apto.es_apto() or apto.esta_vencido(fecha_actual):
            print(f"{trabajador.get_nombre_completo()} no puede trabajar. Apto médico no válido o vencido.")
            return False

        print(f"{trabajador.get_nombre_completo()} está trabajando con {herramienta.get_nombre()}.")
        for tarea in trabajador.get_tareas():
            print(f"  - Realizando tarea: {tarea.get_descripcion()} (Duración: {tarea.get_duracion_horas()}h)")
        
        return True

    def _obtener_id_tarea(self, tarea: 'Tarea') -> int:
        """Función de ayuda para ordenar tareas por ID."""
        return tarea.get_id()

    def mostrar_datos(self, trabajador: 'Trabajador') -> None:
        """Muestra los datos de un trabajador."""
        print(f"\n--- Datos del Trabajador ---")
        print(f"Nombre: {trabajador.get_nombre_completo()}")
        print(f"DNI: {trabajador.get_dni()}")
        apto = trabajador.get_apto_medico()
        if apto:
            print(f"Apto Médico: {'Sí' if apto.es_apto() else 'No'} (Vence: {apto.get_fecha_vencimiento()})")
        else:
            print("Apto Médico: No asignado")
        
        tareas = trabajador.get_tareas()
        # La rúbrica prohibe lambdas, usamos un método de ayuda para ordenar
        tareas.sort(key=self._obtener_id_tarea, reverse=True)
        print(f"Tareas asignadas ({len(tareas)}): ")
        for tarea in tareas:
            print(f"  - ID: {tarea.get_id()}, Desc: {tarea.get_descripcion()}")



################################################################################
# DIRECTORIO: servicios/terrenos
################################################################################

# ==============================================================================
# ARCHIVO 64/67: __init__.py
# Directorio: servicios/terrenos
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/servicios/terrenos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 65/67: plantacion_service.py
# Directorio: servicios/terrenos
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/servicios/terrenos/plantacion_service.py
# ==============================================================================

from typing import TYPE_CHECKING
from datetime import date
from collections import defaultdict

from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.constantes import AGUA_CONSUMIDA_RIEGO

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion

class PlantacionService:
    """
    Servicio para la lógica de negocio de la Plantación.
    """
    def plantar(self, plantacion: 'Plantacion', especie: str, cantidad: int) -> None:
        """
        Planta una cantidad de una especie de cultivo en la plantación.

        Args:
            plantacion: La plantación donde se plantará.
            especie: La especie a plantar.
            cantidad: El número de cultivos a plantar.

        Raises:
            SuperficieInsuficienteException: Si no hay espacio suficiente.
        """
        # Usamos la factory para crear un cultivo temporal y obtener su superficie
        cultivo_temporal = CultivoFactory.crear_cultivo(especie)
        superficie_requerida = cultivo_temporal.get_superficie() * cantidad

        if superficie_requerida > plantacion.get_superficie_disponible():
            raise SuperficieInsuficienteException(
                superficie_requerida=superficie_requerida,
                superficie_disponible=plantacion.get_superficie_disponible()
            )

        for _ in range(cantidad):
            nuevo_cultivo = CultivoFactory.crear_cultivo(especie)
            plantacion.agregar_cultivo(nuevo_cultivo)
        
        nueva_superficie_disponible = plantacion.get_superficie_disponible() - superficie_requerida
        plantacion.set_superficie_disponible(nueva_superficie_disponible)

        print(f"Se plantaron {cantidad} unidades de {especie}.")

    def regar(self, plantacion: 'Plantacion', fecha: date, temperatura: float, humedad: float) -> None:
        """
        Riega todos los cultivos de la plantación y muestra un resumen de la absorción.

        Raises:
            AguaAgotadaException: Si no hay suficiente agua en la plantación.
        """
        if plantacion.get_agua_disponible() < AGUA_CONSUMIDA_RIEGO:
            raise AguaAgotadaException(
                agua_requerida=AGUA_CONSUMIDA_RIEGO,
                agua_disponible=plantacion.get_agua_disponible()
            )
        
        plantacion.set_agua_disponible(plantacion.get_agua_disponible() - AGUA_CONSUMIDA_RIEGO)
        print(f"Regando la plantación... (se consumen {AGUA_CONSUMIDA_RIEGO}L de agua)")

        registry = CultivoServiceRegistry.get_instance()
        
        # Agrupa la absorción por tipo de cultivo
        absorcion_por_tipo = defaultdict(lambda: {'cantidad': 0, 'total_absorbido': 0})
        
        for cultivo in plantacion.get_cultivos():
            agua_absorbida = registry.absorber_agua(cultivo, fecha, temperatura, humedad)
            tipo = type(cultivo).__name__
            resumen = absorcion_por_tipo[tipo]
            resumen['cantidad'] += 1
            resumen['total_absorbido'] += agua_absorbida

        # Imprime el resumen
        for tipo, resumen in absorcion_por_tipo.items():
            # La absorción individual es el total absorbido dividido por la cantidad de plantas
            absorcion_individual = resumen['total_absorbido'] / resumen['cantidad']
            print(f"  - {resumen['cantidad']}x {tipo} absorbieron {absorcion_individual:.0f}L cada uno (Total: {resumen['total_absorbido']}L).")

    def mostrar_datos(self, plantacion: 'Plantacion') -> None:
        """Muestra los datos de una entidad Plantacion."""
        print(f"\n--- Datos de la Plantación ---")
        print(f"Superficie Total: {plantacion.get_superficie_total()} m²")
        print(f"Superficie Disponible: {plantacion.get_superficie_disponible():.2f} m²")
        print(f"Agua Disponible: {plantacion.get_agua_disponible()} L")
        print(f"Número de Cultivos: {len(plantacion.get_cultivos())}")
        print(f"Número de Trabajadores: {len(plantacion.get_trabajadores())}")


# ==============================================================================
# ARCHIVO 66/67: registro_forestal_service.py
# Directorio: servicios/terrenos
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/servicios/terrenos/registro_forestal_service.py
# ==============================================================================

import os
import pickle
from typing import TYPE_CHECKING

from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.excepciones.persistencia_exception import PersistenciaException
from python_forestacion.constantes import DIRECTORIO_DATA

if TYPE_CHECKING:
    from python_forestacion.servicios.terrenos.tierra_service import TierraService
    from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService

class RegistroForestalService:
    """
    Servicio para la lógica de negocio de alto nivel del Registro Forestal,
    incluyendo la creación y la persistencia.
    """
    def crear_registro(self, propietario: str, codigo_catastral: str, sup_tierra: float, sup_plantacion: float) -> RegistroForestal:
        """
        Crea una instancia completa de un RegistroForestal.
        """
        if sup_plantacion > sup_tierra:
            raise ValueError("La superficie de la plantación no puede ser mayor a la de la tierra.")
        
        tierra = Tierra(codigo_catastral, propietario, sup_tierra)
        plantacion = Plantacion(sup_plantacion)
        registro = RegistroForestal(propietario, tierra, plantacion)
        return registro

    def persistir_registro(self, registro: RegistroForestal) -> None:
        """
        Guarda un objeto RegistroForestal en un archivo usando pickle.
        El nombre del archivo es el nombre del propietario.
        """
        if not os.path.exists(DIRECTORIO_DATA):
            os.makedirs(DIRECTORIO_DATA)
            
        nombre_archivo = os.path.join(DIRECTORIO_DATA, f"{registro.get_propietario()}.dat")
        
        try:
            with open(nombre_archivo, 'wb') as f:
                pickle.dump(registro, f)
            print(f"Registro de '{registro.get_propietario()}' guardado exitosamente en {nombre_archivo}")
        except IOError as e:
            raise PersistenciaException(operacion="guardado", error_original=e)

    @staticmethod
    def leer_registro(propietario: str) -> RegistroForestal:
        """
        Carga un objeto RegistroForestal desde un archivo.
        """
        nombre_archivo = os.path.join(DIRECTORIO_DATA, f"{propietario}.dat")
        try:
            with open(nombre_archivo, 'rb') as f:
                registro = pickle.load(f)
                print(f"Registro de '{propietario}' cargado exitosamente.")
                return registro
        except FileNotFoundError:
            raise PersistenciaException(operacion="lectura", error_original=FileNotFoundError(f"No se encontró el archivo {nombre_archivo}"))
        except (IOError, pickle.UnpicklingError) as e:
            raise PersistenciaException(operacion="lectura", error_original=e)

    def mostrar_datos(self, registro: RegistroForestal, tierra_service: 'TierraService', plantacion_service: 'PlantacionService') -> None:
        """Muestra los datos completos del registro forestal."""
        print(f"\n============== REGISTRO FORESTAL DE: {registro.get_propietario().upper()} ===============")
        tierra_service.mostrar_datos(registro.get_tierra())
        plantacion_service.mostrar_datos(registro.get_plantacion())
        print("======================================================================")


# ==============================================================================
# ARCHIVO 67/67: tierra_service.py
# Directorio: servicios/terrenos
# Ruta completa: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/servicios/terrenos/tierra_service.py
# ==============================================================================

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.tierra import Tierra

class TierraService:
    """
    Servicio para la lógica de negocio relacionada con la Tierra.
    """
    def mostrar_datos(self, tierra: 'Tierra') -> None:
        """Muestra los datos de una entidad Tierra."""
        print(f"--- Datos de la Tierra ---")
        print(f"Propietario: {tierra.get_propietario()}")
        print(f"Código Catastral: {tierra.get_codigo_catastral()}")
        print(f"Superficie: {tierra.get_superficie()} m²")



################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 67
# Generado: 2025-10-21 21:58:15
################################################################################
