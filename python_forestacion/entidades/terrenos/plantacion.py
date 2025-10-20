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
