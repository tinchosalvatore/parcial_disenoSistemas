from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.constantes import AGUA_INICIAL_OLIVO, SUPERFICIE_OLIVO
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna


class Olivo(Arbol):
    """
    Clase concreta para el cultivo de Olivo.
    """
    def __init__(self, tipo_aceituna: TipoAceituna):
        """
        Inicializa un olivo.

        Args:
            tipo_aceituna: El tipo de aceituna que produce el olivo.
        """
        super().__init__(agua=AGUA_INICIAL_OLIVO, superficie=SUPERFICIE_OLIVO)
        self._tipo_aceituna = tipo_aceituna

    def get_tipo_aceituna(self) -> TipoAceituna:
        """Retorna el tipo de aceituna que produce el olivo."""
        return self._tipo_aceituna
