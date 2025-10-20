from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class AbsorcionAguaStrategy(ABC):
    """
    Interfaz (Strategy) para definir diferentes algoritmos de absorción de agua.
    """
    @abstractmethod
    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        """
        Calcula la cantidad de agua absorbida por un cultivo.

        Args:
            fecha: La fecha actual.
            temperatura: La temperatura actual.
            humedad: La humedad actual.
            cultivo: El cultivo que absorbe el agua.

        Returns:
            La cantidad de agua absorbida en litros.
        """
        pass
