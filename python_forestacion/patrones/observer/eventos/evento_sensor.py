from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class EventoSensor:
    """Representa un evento de un sensor con un valor y una fecha."""
    valor: float
    fecha: datetime
