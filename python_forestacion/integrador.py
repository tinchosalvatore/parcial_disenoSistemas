"""
Archivo integrador generado automaticamente
Directorio: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion
Fecha: 2025-10-21 18:14:55
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: constantes.py
# Ruta: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/constantes.py
# ================================================================================

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

