from typing import List, Optional, TYPE_CHECKING

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
