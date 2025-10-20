from python_forestacion.excepciones.forestacion_exception import ForestacionException

class SuperficieInsuficienteException(ForestacionException):
    """
    Excepción lanzada cuando no hay suficiente superficie para una operación.
    """
    def __init__(self, superficie_requerida: float, superficie_disponible: float):
        user_msg = f"No hay suficiente superficie. Se requieren {superficie_requerida:.2f}m² pero solo hay {superficie_disponible:.2f}m² disponibles."
        tech_msg = f"Superficie requerida ({superficie_requerida}) > disponible ({superficie_disponible})"
        super().__init__(user_msg, tech_msg)
        self.superficie_requerida = superficie_requerida
        self.superficie_disponible = superficie_disponible
