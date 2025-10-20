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
