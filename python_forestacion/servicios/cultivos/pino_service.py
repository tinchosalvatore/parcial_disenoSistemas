from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.pino import Pino

class PinoService(ArbolService):
    """
    Servicio específico para la lógica de negocio del Pino.
    """
    def __init__(self):
        # Inyecta la estrategia de absorción estacional, específica para árboles.
        super().__init__(AbsorcionSeasonalStrategy())

    def mostrar_datos(self, cultivo: 'Pino') -> None:
        """Muestra los datos generales y los específicos del Pino."""
        super().mostrar_datos(cultivo)
        print(f"Variedad: {cultivo.get_variedad()}")
