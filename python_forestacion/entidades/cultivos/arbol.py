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
