from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class EventoPlantacion:
    """Representa un evento ocurrido en una plantación."""
    tipo_evento: str
    fecha: date
    descripcion: str
