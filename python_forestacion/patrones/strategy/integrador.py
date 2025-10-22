"""
Archivo integrador generado automaticamente
Directorio: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/patrones/strategy
Fecha: 2025-10-21 21:58:15
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/patrones/strategy/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: absorcion_agua_strategy.py
# Ruta: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/patrones/strategy/absorcion_agua_strategy.py
# ================================================================================

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


