"""
Archivo integrador generado automaticamente
Directorio: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/excepciones
Fecha: 2025-10-21 21:58:15
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/excepciones/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/6: agua_agotada_exception.py
# Ruta: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/excepciones/agua_agotada_exception.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/6: forestacion_exception.py
# Ruta: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/excepciones/forestacion_exception.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 4/6: mensajes_exception.py
# Ruta: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/excepciones/mensajes_exception.py
# ================================================================================

"""
Centraliza los mensajes de error para las excepciones personalizadas.
"""


# ================================================================================
# ARCHIVO 5/6: persistencia_exception.py
# Ruta: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/excepciones/persistencia_exception.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 6/6: superficie_insuficiente_exception.py
# Ruta: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/excepciones/superficie_insuficiente_exception.py
# ================================================================================

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


