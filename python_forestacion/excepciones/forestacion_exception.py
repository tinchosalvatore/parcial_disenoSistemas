class ForestacionException(Exception):
    """
    Clase base para todas las excepciones personalizadas del proyecto.
    Permite diferenciar nuestros errores de los errores nativos de Python.
    """
    def __init__(self, user_message: str, tech_message: str):
        """
        Args:
            user_message: Mensaje claro para el usuario final.
            tech_message: Mensaje técnico para desarrolladores (logs).
        """
        super().__init__(tech_message)
        self._user_message = user_message
        self._tech_message = tech_message

    def get_user_message(self) -> str:
        return self._user_message

    def get_tech_message(self) -> str:
        return self._tech_message
