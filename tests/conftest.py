import sys
import os
import pytest
from datetime import date, timedelta

# Añadir el directorio raíz del proyecto al sys.path para que pytest encuentre los módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.apto_medico import AptoMedico

@pytest.fixture
def plantacion_default() -> Plantacion:
    """Fixture que retorna una plantación de 1000 m² con 500L de agua."""
    p = Plantacion(superficie=1000.0)
    p.set_agua_disponible(500.0)
    return p

@pytest.fixture
def trabajador_default() -> Trabajador:
    """Fixture que retorna un trabajador simple."""
    return Trabajador(nombre="Juan", apellido="Perez", dni="30123456")

@pytest.fixture
def trabajador_con_apto(trabajador_default: Trabajador) -> Trabajador:
    """Fixture que retorna un trabajador con un apto médico válido."""
    apto = AptoMedico(
        fecha_emision=date.today(),
        fecha_vencimiento=date.today() + timedelta(days=365),
        es_apto=True
    )
    trabajador_default.set_apto_medico(apto)
    return trabajador_default

@pytest.fixture(autouse=True)
def limpiar_directorio_data():
    """Limpia los archivos .dat generados por los tests en el directorio data/."""
    yield
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    if not os.path.exists(data_dir):
        return
    for filename in os.listdir(data_dir):
        if filename.endswith('.dat'):
            os.remove(os.path.join(data_dir, filename))
