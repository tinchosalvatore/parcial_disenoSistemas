from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class CultivoService(ABC):
    """
    Clase base abstracta para los servicios de cultivo.
    Contiene la lógica de negocio común y utiliza el patrón Strategy para la absorción de agua.
    """
    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        """
        Inyecta la estrategia de absorción de agua.

        Args:
            estrategia_absorcion: La estrategia a utilizar para calcular la absorción.
        """
        self._estrategia_absorcion = estrategia_absorcion

    def absorver_agua(self, cultivo: 'Cultivo', fecha: date, temperatura: float, humedad: float) -> int:
        """
        Calcula y aplica la absorción de agua a un cultivo usando la estrategia inyectada.
        """
        agua_absorbida = self._estrategia_absorcion.calcular_absorcion(
            fecha, temperatura, humedad, cultivo
        )
        cultivo.set_agua(cultivo.get_agua() + agua_absorbida)
        return agua_absorbida

    @abstractmethod
    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """Muestra los datos específicos de un cultivo."""
        print(f"Agua: {cultivo.get_agua()}L, Superficie: {cultivo.get_superficie()}m²")
