class Tierra:
    """
    Representa una porción de tierra con su identificación catastral y propietario.
    """
    def __init__(self, codigo_catastral: str, propietario: str, superficie: float):
        """
        Inicializa la tierra. Y establece algunas excepciones basicas

        Args:
            codigo_catastral: Identificador único del catastro.
            propietario: Nombre del dueño de la tierra.
            superficie: Superficie total de la tierra en metros cuadrados.
        """
        self._codigo_catastral = codigo_catastral
        self._propietario = propietario
        self._superficie = superficie

    def get_codigo_catastral(self) -> str:
        return self._codigo_catastral

    def set_codigo_catastral(self, codigo_catastral: str) -> None:
        if not codigo_catastral:
            raise ValueError("El código catastral no puede estar vacío.")
        self._codigo_catastral = codigo_catastral

    def get_propietario(self) -> str:
        return self._propietario

    def set_propietario(self, propietario: str) -> None:
        if not propietario:
            raise ValueError("El propietario no puede estar vacío.")
        self._propietario = propietario

    def get_superficie(self) -> float:
        return self._superficie

    def set_superficie(self, superficie: float) -> None:
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero.")
        self._superficie = superficie
