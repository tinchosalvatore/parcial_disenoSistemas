from abc import ABC

class Cultivo(ABC):
    """
    Clase abstracta base para todos los tipos de cultivos.
    Define la estructura y atributos comunes que cualquier cultivo debe tener.
    Las entidades son DTOs (Data Transfer Objects), solo contienen datos.
    """
    def __init__(self, agua: float, superficie: float):
        """
        Inicializa un cultivo con una cantidad de agua y superficie requerida.

        Args:
            agua: Cantidad de agua inicial del cultivo en litros.
            superficie: Superficie que ocupa el cultivo en metros cuadrados.
        """
        self._agua = agua
        self._superficie = superficie

    def get_agua(self) -> float:
        """Retorna la cantidad de agua actual del cultivo."""
        return self._agua

    def set_agua(self, agua: float) -> None:
        """
        Establece la cantidad de agua del cultivo.
        No permite valores negativos.
        """
        if agua < 0:
            raise ValueError("La cantidad de agua no puede ser negativa.")
        self._agua = agua

    def get_superficie(self) -> float:
        """Retorna la superficie que ocupa el cultivo."""
        return self._superficie

    def set_superficie(self, superficie: float) -> None:
        """
        Establece la superficie del cultivo.
        No permite valores negativos o cero.
        """
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero.")
        self._superficie = superficie
