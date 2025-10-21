"""
Archivo integrador generado automaticamente
Directorio: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/entidades/cultivos
Fecha: 2025-10-21 18:14:55
Total de archivos integrados: 9
"""

# ================================================================================
# ARCHIVO 1/9: __init__.py
# Ruta: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/entidades/cultivos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/9: arbol.py
# Ruta: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/entidades/cultivos/arbol.py
# ================================================================================

from abc import ABC
from python_forestacion.entidades.cultivos.cultivo import Cultivo

class Arbol(Cultivo, ABC):
    """
    Clase abstracta base para todos los cultivos de tipo Árbol.
    Hereda de Cultivo y sirve como categoría para agrupar árboles.
    """
    def __init__(self, agua: float, superficie: float):
        """
        Inicializa un árbol.

        Args:
            agua: Cantidad de agua inicial en litros.
            superficie: Superficie que ocupa en metros cuadrados.
        """
        super().__init__(agua, superficie)


# ================================================================================
# ARCHIVO 3/9: cultivo.py
# Ruta: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/entidades/cultivos/cultivo.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 4/9: hortaliza.py
# Ruta: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/entidades/cultivos/hortaliza.py
# ================================================================================

from abc import ABC
from python_forestacion.entidades.cultivos.cultivo import Cultivo

class Hortaliza(Cultivo, ABC):
    """
    Clase abstracta base para todos los cultivos de tipo Hortaliza.
    Añade la especificidad de si se cultiva en invernadero.
    """
    def __init__(self, agua: float, superficie: float, invernadero: bool):
        """
        Inicializa una hortaliza.

        Args:
            agua: Cantidad de agua inicial en litros.
            superficie: Superficie que ocupa en metros cuadrados.
            invernadero: True si requiere invernadero, False en caso contrario.
        """
        super().__init__(agua, superficie)
        self._invernadero = invernadero

    def requiere_invernadero(self) -> bool:
        """Retorna True si la hortaliza requiere invernadero."""
        return self._invernadero


# ================================================================================
# ARCHIVO 5/9: lechuga.py
# Ruta: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/entidades/cultivos/lechuga.py
# ================================================================================

from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import AGUA_INICIAL_LECHUGA, SUPERFICIE_LECHUGA

class Lechuga(Hortaliza):
    """
    Clase concreta para el cultivo de Lechuga.
    """
    def __init__(self, tipo_hoja: str):
        """
        Inicializa una lechuga.

        Args:
            tipo_hoja: El tipo de hoja de la lechuga (ej: 'Rizada').
        """
        super().__init__(
            agua=AGUA_INICIAL_LECHUGA, 
            superficie=SUPERFICIE_LECHUGA, 
            invernadero=True
        )
        self._tipo_hoja = tipo_hoja

    def get_tipo_hoja(self) -> str:
        """Retorna el tipo de hoja de la lechuga."""
        return self._tipo_hoja


# ================================================================================
# ARCHIVO 6/9: olivo.py
# Ruta: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/entidades/cultivos/olivo.py
# ================================================================================

from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.constantes import AGUA_INICIAL_OLIVO, SUPERFICIE_OLIVO
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna


class Olivo(Arbol):
    """
    Clase concreta para el cultivo de Olivo.
    """
    def __init__(self, tipo_aceituna: TipoAceituna):
        """
        Inicializa un olivo.

        Args:
            tipo_aceituna: El tipo de aceituna que produce el olivo.
        """
        super().__init__(agua=AGUA_INICIAL_OLIVO, superficie=SUPERFICIE_OLIVO)
        self._tipo_aceituna = tipo_aceituna

    def get_tipo_aceituna(self) -> TipoAceituna:
        """Retorna el tipo de aceituna que produce el olivo."""
        return self._tipo_aceituna


# ================================================================================
# ARCHIVO 7/9: pino.py
# Ruta: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/entidades/cultivos/pino.py
# ================================================================================

from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.constantes import AGUA_INICIAL_PINO, SUPERFICIE_PINO

class Pino(Arbol):
    """
    Clase concreta para el cultivo de Pino.
    """
    def __init__(self, variedad: str):
        """
        Inicializa un pino con una variedad específica.

        Args:
            variedad: La variedad del pino (ej: 'Parana').
        """
        super().__init__(agua=AGUA_INICIAL_PINO, superficie=SUPERFICIE_PINO)
        self._variedad = variedad

    def get_variedad(self) -> str:
        """Retorna la variedad del pino."""
        return self._variedad


# ================================================================================
# ARCHIVO 8/9: tipo_aceituna.py
# Ruta: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/entidades/cultivos/tipo_aceituna.py
# ================================================================================

from enum import Enum, auto

class TipoAceituna(Enum):
    """
    Enum para los tipos de aceituna que puede producir un Olivo.
    """
    ARBEQUINA = auto()
    PICUAL = auto()
    MANZANILLA = auto()


# ================================================================================
# ARCHIVO 9/9: zanahoria.py
# Ruta: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/entidades/cultivos/zanahoria.py
# ================================================================================

from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import AGUA_INICIAL_ZANAHORIA, SUPERFICIE_ZANAHORIA

class Zanahoria(Hortaliza):
    """
    Clase concreta para el cultivo de Zanahoria.
    """
    def __init__(self, color: str):
        """
        Inicializa una zanahoria.

        Args:
            color: El color de la zanahoria (ej: 'Naranja').
        """
        super().__init__(
            agua=AGUA_INICIAL_ZANAHORIA, 
            superficie=SUPERFICIE_ZANAHORIA, 
            invernadero=False
        )
        self._color = color

    def get_color(self) -> str:
        """Retorna el color de la zanahoria."""
        return self._color


