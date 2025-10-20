import pytest
from datetime import date
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.constantes import AGUA_CONSUMIDA_RIEGO

@pytest.fixture
def plantacion_service() -> PlantacionService:
    """Fixture para el PlantacionService."""
    return PlantacionService()

@pytest.fixture
def plantacion_pequena() -> Plantacion:
    """Fixture para una plantación pequeña de 10m²."""
    p = Plantacion(superficie=10.0)
    p.set_agua_disponible(100.0) # Le damos algo de agua inicial
    return p

def test_plantar_exitosamente(plantacion_service: PlantacionService, plantacion_pequena: Plantacion):
    """Prueba que los cultivos se pueden plantar si hay espacio."""
    # Pino requiere 2.0 m²
    plantacion_service.plantar(plantacion_pequena, "Pino", 2) # 2 Pinos * 2.0 m²/u = 4.0 m²
    assert len(plantacion_pequena.get_cultivos()) == 2
    assert plantacion_pequena.get_superficie_disponible() == 6.0

def test_plantar_sin_superficie_suficiente(plantacion_service: PlantacionService, plantacion_pequena: Plantacion):
    """Prueba que se lanza SuperficieInsuficienteException si no hay espacio."""
    # Olivo requiere 3.0 m²
    with pytest.raises(SuperficieInsuficienteException) as excinfo:
        plantacion_service.plantar(plantacion_pequena, "Olivo", 4)  # 4 Olivos * 3.0 m²/u = 12.0 m² > 10.0 m²
    
    # Accedemos a los atributos directamente, no a getters
    assert excinfo.value.superficie_requerida == 12.0
    assert excinfo.value.superficie_disponible == 10.0

def test_regar_exitosamente(plantacion_service: PlantacionService, plantacion_pequena: Plantacion):
    """Prueba que el riego funciona si hay suficiente agua."""
    initial_water = plantacion_pequena.get_agua_disponible()
    # El método regar real necesita fecha, temperatura y humedad
    plantacion_service.regar(plantacion_pequena, date.today(), 25.0, 40.0)
    assert plantacion_pequena.get_agua_disponible() < initial_water

def test_regar_sin_agua_suficiente(plantacion_service: PlantacionService, plantacion_pequena: Plantacion):
    """Prueba que se lanza AguaAgotadaException si no hay suficiente agua."""
    # AGUA_CONSUMIDA_RIEGO es 10, ponemos menos que eso
    plantacion_pequena.set_agua_disponible(AGUA_CONSUMIDA_RIEGO - 1)
    
    with pytest.raises(AguaAgotadaException):
        plantacion_service.regar(plantacion_pequena, date.today(), 25.0, 40.0)
