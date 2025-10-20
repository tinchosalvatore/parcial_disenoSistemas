from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import AGUA_INICIAL_LECHUGA, SUPERFICIE_LECHUGA

class Lechuga(Hortaliza):
    """
    Clase concreta para el cultivo de Lechuga.
    """
    def __init__(self, tipo_hoja: str):
        """
        Inicializa una lechuga.

        Args:
            tipo_hoja: El tipo de hoja de la lechuga (ej: 'Rizada').
        """
        super().__init__(
            agua=AGUA_INICIAL_LECHUGA, 
            superficie=SUPERFICIE_LECHUGA, 
            invernadero=True
        )
        self._tipo_hoja = tipo_hoja

    def get_tipo_hoja(self) -> str:
        """Retorna el tipo de hoja de la lechuga."""
        return self._tipo_hoja
