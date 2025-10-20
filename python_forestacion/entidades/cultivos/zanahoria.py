from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import AGUA_INICIAL_ZANAHORIA, SUPERFICIE_ZANAHORIA

class Zanahoria(Hortaliza):
    """
    Clase concreta para el cultivo de Zanahoria.
    """
    def __init__(self, color: str):
        """
        Inicializa una zanahoria.

        Args:
            color: El color de la zanahoria (ej: 'Naranja').
        """
        super().__init__(
            agua=AGUA_INICIAL_ZANAHORIA, 
            superficie=SUPERFICIE_ZANAHORIA, 
            invernadero=False
        )
        self._color = color

    def get_color(self) -> str:
        """Retorna el color de la zanahoria."""
        return self._color
