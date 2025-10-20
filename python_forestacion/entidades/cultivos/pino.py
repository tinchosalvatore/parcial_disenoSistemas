from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.constantes import AGUA_INICIAL_PINO, SUPERFICIE_PINO

class Pino(Arbol):
    """
    Clase concreta para el cultivo de Pino.
    """
    def __init__(self, variedad: str):
        """
        Inicializa un pino con una variedad específica.

        Args:
            variedad: La variedad del pino (ej: 'Parana').
        """
        super().__init__(agua=AGUA_INICIAL_PINO, superficie=SUPERFICIE_PINO)
        self._variedad = variedad

    def get_variedad(self) -> str:
        """Retorna la variedad del pino."""
        return self._variedad
