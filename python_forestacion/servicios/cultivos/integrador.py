"""
Archivo integrador generado automaticamente
Directorio: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/servicios/cultivos
Fecha: 2025-10-21 21:58:15
Total de archivos integrados: 8
"""

# ================================================================================
# ARCHIVO 1/8: __init__.py
# Ruta: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/servicios/cultivos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/8: arbol_service.py
# Ruta: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/servicios/cultivos/arbol_service.py
# ================================================================================

from abc import ABC
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

class ArbolService(CultivoService, ABC):
    """
    Clase base para los servicios de árboles.
    """
    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        super().__init__(estrategia_absorcion)


# ================================================================================
# ARCHIVO 3/8: cultivo_service.py
# Ruta: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/servicios/cultivos/cultivo_service.py
# ================================================================================

from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class CultivoService(ABC):
    """
    Clase base abstracta para los servicios de cultivo.
    Contiene la lógica de negocio común y utiliza el patrón Strategy para la absorción de agua.
    """
    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        """
        Inyecta la estrategia de absorción de agua.

        Args:
            estrategia_absorcion: La estrategia a utilizar para calcular la absorción.
        """
        self._estrategia_absorcion = estrategia_absorcion

    def absorver_agua(self, cultivo: 'Cultivo', fecha: date, temperatura: float, humedad: float) -> int:
        """
        Calcula y aplica la absorción de agua a un cultivo usando la estrategia inyectada.
        """
        agua_absorbida = self._estrategia_absorcion.calcular_absorcion(
            fecha, temperatura, humedad, cultivo
        )
        cultivo.set_agua(cultivo.get_agua() + agua_absorbida)
        return agua_absorbida

    @abstractmethod
    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """Muestra los datos específicos de un cultivo."""
        print(f"Agua: {cultivo.get_agua()}L, Superficie: {cultivo.get_superficie()}m²")


# ================================================================================
# ARCHIVO 4/8: cultivo_service_registry.py
# Ruta: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/servicios/cultivos/cultivo_service_registry.py
# ================================================================================

from threading import Lock
from datetime import date
from typing import TYPE_CHECKING, Dict, Type, Callable

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.cultivos.pino import Pino
    from python_forestacion.entidades.cultivos.olivo import Olivo
    from python_forestacion.entidades.cultivos.lechuga import Lechuga
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
    from python_forestacion.servicios.cultivos.pino_service import PinoService
    from python_forestacion.servicios.cultivos.olivo_service import OlivoService
    from python_forestacion.servicios.cultivos.lechuga_service import LechugaService
    from python_forestacion.servicios.cultivos.zanahoria_service import ZanahoriaService

class CultivoServiceRegistry:
    """
    Implementa los patrones Singleton y Registry.
    - Singleton: Asegura una única instancia de esta clase.
    - Registry: Proporciona un punto central para acceder a los servicios de cultivo
      y realizar dispatch polimórfico sin usar isinstance().
    """
    _instance = None
    _lock = Lock()

# Esta funciona hace que la clase sea un Singleton
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._inicializar_servicios()
        return cls._instance

    @classmethod
    def get_instance(cls):
        """Punto de acceso global a la instancia Singleton."""
        if cls._instance is None:
            cls()  # Llama a __new__ para crear la instancia si no existe
        return cls._instance

    def _inicializar_servicios(self) -> None:
        """Inicializa y registra todos los servicios de cultivo y sus manejadores."""
        from python_forestacion.entidades.cultivos.pino import Pino
        from python_forestacion.entidades.cultivos.olivo import Olivo
        from python_forestacion.entidades.cultivos.lechuga import Lechuga
        from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
        from python_forestacion.servicios.cultivos.pino_service import PinoService
        from python_forestacion.servicios.cultivos.olivo_service import OlivoService
        from python_forestacion.servicios.cultivos.lechuga_service import LechugaService
        from python_forestacion.servicios.cultivos.zanahoria_service import ZanahoriaService

        # Instanciar servicios
        self._pino_service: 'PinoService' = PinoService()
        self._olivo_service: 'OlivoService' = OlivoService()
        self._lechuga_service: 'LechugaService' = LechugaService()
        self._zanahoria_service: 'ZanahoriaService' = ZanahoriaService()

        # Registrar manejadores (handlers) para cada acción y tipo de cultivo
        self._absorber_agua_handlers: Dict[Type['Cultivo'], Callable] = {
            Pino: self._absorber_agua_pino,
            Olivo: self._absorber_agua_olivo,
            Lechuga: self._absorber_agua_lechuga,
            Zanahoria: self._absorber_agua_zanahoria,
        }
        
        self._mostrar_datos_handlers: Dict[Type['Cultivo'], Callable] = {
            Pino: self._mostrar_datos_pino,
            Olivo: self._mostrar_datos_olivo,
            Lechuga: self._mostrar_datos_lechuga,
            Zanahoria: self._mostrar_datos_zanahoria,
        }

    # --- Métodos públicos de dispatch ---

    def absorber_agua(self, cultivo: 'Cultivo', fecha: date, temperatura: float, humedad: float) -> int:
        """Realiza el dispatch para la acción de absorber agua."""
        handler = self._get_handler_for_cultivo(self._absorber_agua_handlers, cultivo)
        return handler(cultivo, fecha, temperatura, humedad)

    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """Realiza el dispatch para la acción de mostrar datos."""
        handler = self._get_handler_for_cultivo(self._mostrar_datos_handlers, cultivo)
        handler(cultivo)

    # --- Métodos de ayuda ---

    def _get_handler_for_cultivo(self, handlers: dict, cultivo: 'Cultivo') -> Callable:
        """Busca el manejador apropiado para el tipo de cultivo."""
        tipo_cultivo = type(cultivo)
        if tipo_cultivo not in handlers:
            raise ValueError(f"No se encontró un manejador para el tipo de cultivo: {tipo_cultivo.__name__}")
        return handlers[tipo_cultivo]

    # --- Manejadores privados para cada tipo de cultivo y acción ---

    def _absorber_agua_pino(self, cultivo: 'Pino', fecha: date, temperatura: float, humedad: float) -> int:
        return self._pino_service.absorver_agua(cultivo, fecha, temperatura, humedad)

    def _absorber_agua_olivo(self, cultivo: 'Olivo', fecha: date, temperatura: float, humedad: float) -> int:
        return self._olivo_service.absorver_agua(cultivo, fecha, temperatura, humedad)

    def _absorber_agua_lechuga(self, cultivo: 'Lechuga', fecha: date, temperatura: float, humedad: float) -> int:
        return self._lechuga_service.absorver_agua(cultivo, fecha, temperatura, humedad)

    def _absorber_agua_zanahoria(self, cultivo: 'Zanahoria', fecha: date, temperatura: float, humedad: float) -> int:
        return self._zanahoria_service.absorver_agua(cultivo, fecha, temperatura, humedad)

    def _mostrar_datos_pino(self, cultivo: 'Pino') -> None:
        self._pino_service.mostrar_datos(cultivo)

    def _mostrar_datos_olivo(self, cultivo: 'Olivo') -> None:
        self._olivo_service.mostrar_datos(cultivo)

    def _mostrar_datos_lechuga(self, cultivo: 'Lechuga') -> None:
        self._lechuga_service.mostrar_datos(cultivo)

    def _mostrar_datos_zanahoria(self, cultivo: 'Zanahoria') -> None:
        self._zanahoria_service.mostrar_datos(cultivo)


# ================================================================================
# ARCHIVO 5/8: lechuga_service.py
# Ruta: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/servicios/cultivos/lechuga_service.py
# ================================================================================

from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.constantes import ABSORCION_CONSTANTE_LECHUGA

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.lechuga import Lechuga

class LechugaService(CultivoService):
    """
    Servicio específico para la lógica de negocio de la Lechuga.
    """
    def __init__(self):
        # Inyecta la estrategia de absorción constante, específica para hortalizas.
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_CONSTANTE_LECHUGA))

    def mostrar_datos(self, cultivo: 'Lechuga') -> None:
        """Muestra los datos generales y los específicos de la Lechuga."""
        super().mostrar_datos(cultivo)
        print(f"Tipo de hoja: {cultivo.get_tipo_hoja()}")
        print(f"Requiere invernadero: {cultivo.requiere_invernadero()}")


# ================================================================================
# ARCHIVO 6/8: olivo_service.py
# Ruta: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/servicios/cultivos/olivo_service.py
# ================================================================================

from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.olivo import Olivo

class OlivoService(ArbolService):
    """
    Servicio específico para la lógica de negocio del Olivo.
    """
    def __init__(self):
        # Inyecta la estrategia de absorción estacional, específica para árboles.
        super().__init__(AbsorcionSeasonalStrategy())

    def mostrar_datos(self, cultivo: 'Olivo') -> None:
        """Muestra los datos generales y los específicos del Olivo."""
        super().mostrar_datos(cultivo)
        print(f"Tipo de aceituna: {cultivo.get_tipo_aceituna().name}")


# ================================================================================
# ARCHIVO 7/8: pino_service.py
# Ruta: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/servicios/cultivos/pino_service.py
# ================================================================================

from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.pino import Pino

class PinoService(ArbolService):
    """
    Servicio específico para la lógica de negocio del Pino.
    """
    def __init__(self):
        # Inyecta la estrategia de absorción estacional, específica para árboles.
        super().__init__(AbsorcionSeasonalStrategy())

    def mostrar_datos(self, cultivo: 'Pino') -> None:
        """Muestra los datos generales y los específicos del Pino."""
        super().mostrar_datos(cultivo)
        print(f"Variedad: {cultivo.get_variedad()}")


# ================================================================================
# ARCHIVO 8/8: zanahoria_service.py
# Ruta: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/servicios/cultivos/zanahoria_service.py
# ================================================================================

from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.constantes import ABSORCION_CONSTANTE_ZANAHORIA

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria

class ZanahoriaService(CultivoService):
    """
    Servicio específico para la lógica de negocio de la Zanahoria.
    """
    def __init__(self):
        # Inyecta la estrategia de absorción constante con el valor para la zanahoria.
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_CONSTANTE_ZANAHORIA))

    def mostrar_datos(self, cultivo: 'Zanahoria') -> None:
        """Muestra los datos generales y los específicos de la Zanahoria."""
        super().mostrar_datos(cultivo)
        print(f"Color: {cultivo.get_color()}")
        print(f"Requiere invernadero: {cultivo.requiere_invernadero()}")


