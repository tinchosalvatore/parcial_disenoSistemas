"""
Archivo integrador generado automaticamente
Directorio: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/entidades/terrenos
Fecha: 2025-10-21 18:14:55
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/entidades/terrenos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: plantacion.py
# Ruta: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/entidades/terrenos/plantacion.py
# ================================================================================

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.personal.trabajador import Trabajador

class Plantacion:
    """
    Representa una parcela de cultivo dentro de una Tierra.
    Gestiona los cultivos, trabajadores, agua y superficie.
    """
    def __init__(self, superficie: float):
        """
        Inicializa la plantación con una superficie total.

        Args:
            superficie: La superficie total de la plantación en m².
        """
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero.")
        
        self._superficie_total = superficie
        self._superficie_disponible = superficie
        self._agua_disponible = 0.0
        self._cultivos: List['Cultivo'] = []
        self._trabajadores: List['Trabajador'] = []

    def get_superficie_total(self) -> float:
        return self._superficie_total

    def get_superficie_disponible(self) -> float:
        return self._superficie_disponible

    def set_superficie_disponible(self, superficie: float) -> None:
        if superficie < 0:
            raise ValueError("La superficie disponible no puede ser negativa.")
        self._superficie_disponible = superficie

    def get_agua_disponible(self) -> float:
        return self._agua_disponible

    def set_agua_disponible(self, agua: float) -> None:
        if agua < 0:
            raise ValueError("El agua disponible no puede ser negativa.")
        self._agua_disponible = agua

    def get_cultivos(self) -> List['Cultivo']:
        """Retorna una copia de la lista de cultivos para evitar modificaciones externas."""
        return self._cultivos.copy()

    def agregar_cultivo(self, cultivo: 'Cultivo') -> None:
        self._cultivos.append(cultivo)

    def get_trabajadores(self) -> List['Trabajador']:
        """Retorna una copia de la lista de trabajadores."""
        return self._trabajadores.copy()

    def agregar_trabajador(self, trabajador: 'Trabajador') -> None:
        self._trabajadores.append(trabajador)


# ================================================================================
# ARCHIVO 3/4: registro_forestal.py
# Ruta: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/entidades/terrenos/registro_forestal.py
# ================================================================================

from typing import TYPE_CHECKING

# Cuidar imports circulares, es False durante tiempo de ejecucion, pero no para el chequeo de tipos
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
        Inicializa el registro forestal. Tambien chequea la coherencia de los datos sobre el propietario.

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


# ================================================================================
# ARCHIVO 4/4: tierra.py
# Ruta: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/entidades/terrenos/tierra.py
# ================================================================================

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


