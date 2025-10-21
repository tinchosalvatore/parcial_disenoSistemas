from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.constantes import AGUA_INICIAL_OLIVO, SUPERFICIE_OLIVO

class Olivo(Arbol):
    """
    Clase concreta para el cultivo de Olivo.
    """
    def __init__(self, produce_aceitunas: bool):
        """
        Inicializa un olivo. Asignando sus valores magicos correspondiente

        Args:
            produce_aceitunas: True si la variedad produce aceitunas.
        """
        super().__init__(agua=AGUA_INICIAL_OLIVO, superficie=SUPERFICIE_OLIVO)  
        self._produce_aceitunas = produce_aceitunas

    def produce_aceitunas(self) -> bool:
        """Retorna True si el olivo produce aceitunas."""
        return self._produce_aceitunas
