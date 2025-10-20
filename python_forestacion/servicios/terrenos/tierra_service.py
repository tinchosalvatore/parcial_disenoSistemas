from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.tierra import Tierra

class TierraService:
    """
    Servicio para la lógica de negocio relacionada con la Tierra.
    """
    def mostrar_datos(self, tierra: 'Tierra') -> None:
        """Muestra los datos de una entidad Tierra."""
        print(f"--- Datos de la Tierra ---")
        print(f"Propietario: {tierra.get_propietario()}")
        print(f"Código Catastral: {tierra.get_codigo_catastral()}")
        print(f"Superficie: {tierra.get_superficie()} m²")
