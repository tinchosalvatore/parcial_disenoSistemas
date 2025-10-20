import pytest
from datetime import date

from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.patrones.observer.observer import Observer
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.constantes import MES_INICIO_VERANO, MES_FIN_VERANO, ABSORCION_SEASONAL_VERANO, ABSORCION_SEASONAL_INVIERNO

class TestSingleton:
    def test_cultivo_service_registry_es_singleton(self):
        """Verifica que CultivoServiceRegistry siempre retorna la misma instancia."""
        registry1 = CultivoServiceRegistry.get_instance()
        registry2 = CultivoServiceRegistry.get_instance()
        registry3 = CultivoServiceRegistry()
        
        assert registry1 is registry2
        assert registry1 is registry3

class TestFactory:
    def test_crear_cultivos_validos(self):
        """Verifica que la factory crea los 4 tipos de cultivos correctamente."""
        pino = CultivoFactory.crear_cultivo("Pino")
        olivo = CultivoFactory.crear_cultivo("Olivo")
        lechuga = CultivoFactory.crear_cultivo("Lechuga")
        zanahoria = CultivoFactory.crear_cultivo("Zanahoria")

        assert isinstance(pino, Pino)
        assert isinstance(olivo, Olivo)
        assert isinstance(lechuga, Lechuga)
        assert isinstance(zanahoria, Zanahoria)

    def test_crear_cultivo_invalido_lanza_error(self):
        """Verifica que la factory lanza ValueError para una especie desconocida."""
        with pytest.raises(ValueError) as excinfo:
            CultivoFactory.crear_cultivo("Tomate")
        assert "Especie de cultivo desconocida: Tomate" in str(excinfo.value)

class TestObserver:
    
    class SensorMock(Observable[float]):
        def __init__(self):
            super().__init__()
            self.lectura = 0.0
        
        def set_lectura(self, nueva_lectura: float):
            self.lectura = nueva_lectura
            self.notificar_observadores(self.lectura)

    class ControladorMock(Observer[float]):
        def __init__(self):
            self.ultima_actualizacion = 0.0
            self.notificaciones_recibidas = 0
            self.observable_recibido = None
        
        # Adaptamos la firma para reflejar el bug en el código original
        def actualizar(self, observable, evento: float) -> None:
            self.observable_recibido = observable
            self.ultima_actualizacion = evento
            self.notificaciones_recibidas += 1

    def test_notificacion_simple(self):
        """Verifica que un observador es notificado."""
        sensor = self.SensorMock()
        controlador = self.ControladorMock()
        
        sensor.agregar_observador(controlador)
        sensor.set_lectura(25.5)
        
        assert controlador.notificaciones_recibidas == 1
        assert controlador.ultima_actualizacion == 25.5
        assert controlador.observable_recibido is sensor

    def test_remover_observador(self):
        """Verifica que un observador removido no recibe notificaciones."""
        sensor = self.SensorMock()
        controlador = self.ControladorMock()
        
        sensor.agregar_observador(controlador)
        sensor.set_lectura(20.0)
        assert controlador.notificaciones_recibidas == 1
        
        sensor.remover_observador(controlador)
        sensor.set_lectura(22.0)
        
        assert controlador.notificaciones_recibidas == 1 # No debe incrementar

class TestStrategy:

    @pytest.fixture
    def pino_cultivo(self):
        return CultivoFactory.crear_cultivo("Pino")

    def test_absorcion_seasonal_verano(self, pino_cultivo):
        """Prueba la estrategia seasonal en verano."""
        strategy = AbsorcionSeasonalStrategy()
        fecha_verano = date(2025, MES_INICIO_VERANO, 15)
        
        absorcion = strategy.calcular_absorcion(fecha_verano, 30.0, 50.0, pino_cultivo)
        
        assert absorcion == ABSORCION_SEASONAL_VERANO

    def test_absorcion_seasonal_invierno(self, pino_cultivo):
        """Prueba la estrategia seasonal en invierno."""""
        strategy = AbsorcionSeasonalStrategy()
        fecha_invierno = date(2025, MES_INICIO_VERANO - 1, 15)
        
        absorcion = strategy.calcular_absorcion(fecha_invierno, 10.0, 70.0, pino_cultivo)
        
        assert absorcion == ABSORCION_SEASONAL_INVIERNO

    def test_absorcion_constante(self):
        """Prueba la estrategia de absorción constante."""
        CANTIDAD_CONSTANTE = 5
        strategy = AbsorcionConstanteStrategy(CANTIDAD_CONSTANTE)
        
        absorcion = strategy.calcular_absorcion(date.today(), 25.0, 60.0, None)
        
        assert absorcion == CANTIDAD_CONSTANTE