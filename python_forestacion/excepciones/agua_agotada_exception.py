from python_forestacion.excepciones.forestacion_exception import ForestacionException

class AguaAgotadaException(ForestacionException):
    """
    Excepción lanzada cuando no hay suficiente agua para una operación.
    """
    def __init__(self, agua_requerida: float, agua_disponible: float):
        user_msg = f"No hay suficiente agua. Se requieren {agua_requerida:.2f}L pero solo hay {agua_disponible:.2f}L disponibles."
        tech_msg = f"Agua requerida ({agua_requerida}) > disponible ({agua_disponible})"
        super().__init__(user_msg, tech_msg)
        self.agua_requerida = agua_requerida
        self.agua_disponible = agua_disponible
