from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.constantes import ABSORCION_CONSTANTE_ZANAHORIA

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria

class ZanahoriaService(CultivoService):
    """
    Servicio específico para la lógica de negocio de la Zanahoria.
    """
    def __init__(self):
        # Inyecta la estrategia de absorción constante con el valor para la zanahoria.
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_CONSTANTE_ZANAHORIA))

    def mostrar_datos(self, cultivo: 'Zanahoria') -> None:
        """Muestra los datos generales y los específicos de la Zanahoria."""
        super().mostrar_datos(cultivo)
        print(f"Color: {cultivo.get_color()}")
        print(f"Requiere invernadero: {cultivo.requiere_invernadero()}")
