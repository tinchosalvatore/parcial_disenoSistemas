from threading import Lock

class Tarea:
    """
    Representa una tarea que puede ser asignada a un trabajador.
    """
    _next_id = 1
    _lock = Lock()

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
