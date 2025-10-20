import pytest
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.constantes import AGUA_INICIAL_PINO, SUPERFICIE_PINO

# Usamos la factory para crear instancias para los tests
@pytest.fixture
def pino_test() -> Pino:
    return CultivoFactory.crear_cultivo("Pino")

def test_creacion_pino(pino_test: Pino):
    """Verifica que un Pino se crea con los valores correctos."""
    assert isinstance(pino_test, Pino)
    assert pino_test.get_agua() == AGUA_INICIAL_PINO
    assert pino_test.get_superficie() == SUPERFICIE_PINO
    assert pino_test.get_variedad() == "Parana"

def test_creacion_olivo():
    """Verifica que un Olivo se crea correctamente."""
    olivo = CultivoFactory.crear_cultivo("Olivo")
    assert isinstance(olivo, Olivo)
    assert olivo.produce_aceitunas() is True

def test_creacion_lechuga():
    """Verifica que una Lechuga se crea correctamente."""
    lechuga = CultivoFactory.crear_cultivo("Lechuga")
    assert isinstance(lechuga, Lechuga)
    assert lechuga.get_tipo_hoja() == "Rizada"

def test_creacion_zanahoria():
    """Verifica que una Zanahoria se crea correctamente."""
    zanahoria = CultivoFactory.crear_cultivo("Zanahoria")
    assert isinstance(zanahoria, Zanahoria)
    assert zanahoria.get_color() == "Naranja"

def test_set_agua_negativa_lanza_error(pino_test: Pino):
    """Verifica que asignar agua negativa lanza ValueError."""
    with pytest.raises(ValueError) as excinfo:
        pino_test.set_agua(-1.0)
    assert "La cantidad de agua no puede ser negativa" in str(excinfo.value)

def test_set_superficie_negativa_lanza_error(pino_test: Pino):
    """Verifica que asignar superficie negativa lanza ValueError."""
    # La validación está en la entidad base Cultivo, pero la testeamos en una instancia concreta
    with pytest.raises(ValueError) as excinfo:
        pino_test.set_superficie(-1.0)
    assert "La superficie debe ser mayor a cero" in str(excinfo.value)

def test_set_superficie_cero_lanza_error(pino_test: Pino):
    """Verifica que asignar superficie cero lanza ValueError."""
    with pytest.raises(ValueError) as excinfo:
        pino_test.set_superficie(0.0)
    assert "La superficie debe ser mayor a cero" in str(excinfo.value)
