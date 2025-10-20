class Herramienta:
    """
    Representa una herramienta que un trabajador puede utilizar.
    """
    def __init__(self, nombre: str, tipo: str):
        """
        Inicializa la herramienta.

        Args:
            nombre: El nombre de la herramienta (ej: 'Pala').
            tipo: El tipo de herramienta (ej: 'Manual', 'Maquinaria').
        """
        if not nombre or not tipo:
            raise ValueError("El nombre y el tipo no pueden estar vacíos.")
        
        self._nombre = nombre
        self._tipo = tipo

    def get_nombre(self) -> str:
        return self._nombre

    def get_tipo(self) -> str:
        return self._tipo
