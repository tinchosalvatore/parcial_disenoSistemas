from typing import TYPE_CHECKING
from datetime import date

from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.constantes import AGUA_CONSUMIDA_RIEGO

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion

class PlantacionService:
    """
    Servicio para la lógica de negocio de la Plantación.
    """
    def plantar(self, plantacion: 'Plantacion', especie: str, cantidad: int) -> None:
        """
        Planta una cantidad de una especie de cultivo en la plantación.

        Args:
            plantacion: La plantación donde se plantará.
            especie: La especie a plantar.
            cantidad: El número de cultivos a plantar.

        Raises:
            SuperficieInsuficienteException: Si no hay espacio suficiente.
        """
        # Usamos la factory para crear un cultivo temporal y obtener su superficie
        cultivo_temporal = CultivoFactory.crear_cultivo(especie)
        superficie_requerida = cultivo_temporal.get_superficie() * cantidad

        if superficie_requerida > plantacion.get_superficie_disponible():
            raise SuperficieInsuficienteException(
                superficie_requerida=superficie_requerida,
                superficie_disponible=plantacion.get_superficie_disponible()
            )

        for _ in range(cantidad):
            nuevo_cultivo = CultivoFactory.crear_cultivo(especie)
            plantacion.agregar_cultivo(nuevo_cultivo)
        
        nueva_superficie_disponible = plantacion.get_superficie_disponible() - superficie_requerida
        plantacion.set_superficie_disponible(nueva_superficie_disponible)

        print(f"Se plantaron {cantidad} unidades de {especie}.")

    def regar(self, plantacion: 'Plantacion', fecha: date, temperatura: float, humedad: float) -> None:
        """
        Riega todos los cultivos de la plantación.

        Raises:
            AguaAgotadaException: Si no hay suficiente agua en la plantación.
        """
        if plantacion.get_agua_disponible() < AGUA_CONSUMIDA_RIEGO:
            raise AguaAgotadaException(
                agua_requerida=AGUA_CONSUMIDA_RIEGO,
                agua_disponible=plantacion.get_agua_disponible()
            )
        
        plantacion.set_agua_disponible(plantacion.get_agua_disponible() - AGUA_CONSUMIDA_RIEGO)
        print(f"Regando la plantación... (se consumen {AGUA_CONSUMIDA_RIEGO}L de agua)")

        registry = CultivoServiceRegistry.get_instance()
        for cultivo in plantacion.get_cultivos():
            agua_absorbida = registry.absorber_agua(cultivo, fecha, temperatura, humedad)
            print(f"  - Un {type(cultivo).__name__} absorbió {agua_absorbida}L de agua.")

    def mostrar_datos(self, plantacion: 'Plantacion') -> None:
        """Muestra los datos de una entidad Plantacion."""
        print(f"\n--- Datos de la Plantación ---")
        print(f"Superficie Total: {plantacion.get_superficie_total()} m²")
        print(f"Superficie Disponible: {plantacion.get_superficie_disponible():.2f} m²")
        print(f"Agua Disponible: {plantacion.get_agua_disponible()} L")
        print(f"Número de Cultivos: {len(plantacion.get_cultivos())}")
        print(f"Número de Trabajadores: {len(plantacion.get_trabajadores())}")
