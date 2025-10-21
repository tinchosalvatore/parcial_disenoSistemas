"""
Archivo integrador generado automaticamente
Directorio: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/patrones/observer/eventos
Fecha: 2025-10-21 18:14:55
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/patrones/observer/eventos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: evento_plantacion.py
# Ruta: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/patrones/observer/eventos/evento_plantacion.py
# ================================================================================

from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class EventoPlantacion:
    """Representa un evento ocurrido en una plantación."""
    tipo_evento: str
    fecha: date
    descripcion: str


# ================================================================================
# ARCHIVO 3/3: evento_sensor.py
# Ruta: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/patrones/observer/eventos/evento_sensor.py
# ================================================================================

from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class EventoSensor:
    """Representa un evento de un sensor con un valor y una fecha."""
    valor: float
    fecha: datetime


