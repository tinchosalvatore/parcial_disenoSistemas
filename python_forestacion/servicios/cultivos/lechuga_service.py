from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.constantes import ABSORCION_CONSTANTE_LECHUGA

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.lechuga import Lechuga

class LechugaService(CultivoService):
    """
    Servicio específico para la lógica de negocio de la Lechuga.
    """
    def __init__(self):
        # Inyecta la estrategia de absorción constante, específica para hortalizas.
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_CONSTANTE_LECHUGA))

    def mostrar_datos(self, cultivo: 'Lechuga') -> None:
        """Muestra los datos generales y los específicos de la Lechuga."""
        super().mostrar_datos(cultivo)
        print(f"Tipo de hoja: {cultivo.get_tipo_hoja()}")
        print(f"Requiere invernadero: {cultivo.requiere_invernadero()}")
