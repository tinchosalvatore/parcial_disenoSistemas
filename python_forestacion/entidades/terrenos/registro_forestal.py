from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.tierra import Tierra
    from python_forestacion.entidades.terrenos.plantacion import Plantacion

class RegistroForestal:
    """
    Entidad raíz que representa una finca completa.
    Agrupa una Tierra y una Plantación.
    """
    def __init__(self, propietario: str, tierra: 'Tierra', plantacion: 'Plantacion'):
        """
        Inicializa el registro forestal.

        Args:
            propietario: Nombre del propietario del registro.
            tierra: La entidad Tierra asociada.
            plantacion: La entidad Plantacion asociada.
        """
        if not propietario:
            raise ValueError("El propietario no puede estar vacío.")
        if tierra.get_propietario() != propietario:
            raise ValueError("El propietario del registro debe coincidir con el de la tierra.")

        self._propietario = propietario
        self._tierra = tierra
        self._plantacion = plantacion

    def get_propietario(self) -> str:
        return self._propietario

    def get_tierra(self) -> 'Tierra':
        return self._tierra

    def get_plantacion(self) -> 'Plantacion':
        return self._plantacion
