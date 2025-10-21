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
