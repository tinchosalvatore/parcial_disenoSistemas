from python_forestacion.excepciones.forestacion_exception import ForestacionException

class PersistenciaException(ForestacionException):
    """
    Excepción lanzada durante errores de guardado o carga de datos.
    """
    def __init__(self, operacion: str, error_original: Exception):
        user_msg = f"Ocurrió un error durante la operación de {operacion}."
        tech_msg = f"Error en {operacion}: {error_original}"
        super().__init__(user_msg, tech_msg)
        self.operacion = operacion
        self.error_original = error_original
