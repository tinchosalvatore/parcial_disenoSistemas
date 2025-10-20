import pytest
import os
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService
from python_forestacion.excepciones.persistencia_exception import PersistenciaException
from python_forestacion.constantes import DIRECTORIO_DATA

@pytest.fixture
def registro_service() -> RegistroForestalService:
    return RegistroForestalService()

@pytest.fixture
def registro_completo(registro_service: RegistroForestalService):
    """Fixture para un objeto RegistroForestal completo y válido."""
    return registro_service.crear_registro(
        propietario="Tester",
        codigo_catastral="ABC-999",
        sup_tierra=1000.0,
        sup_plantacion=500.0
    )

def test_persistir_y_leer_registro(registro_service: RegistroForestalService, registro_completo):
    """Prueba que un registro forestal se puede persistir y leer correctamente."""
    propietario = registro_completo.get_propietario()
    # El servicio usa la extensión .dat internamente
    ruta_archivo = os.path.join(DIRECTORIO_DATA, f"{propietario}.dat")

    # Asegurarse de que el archivo no existe antes de la prueba
    if os.path.exists(ruta_archivo):
        os.remove(ruta_archivo)

    try:
        # Usar el nombre de método correcto: persistir_registro
        registro_service.persistir_registro(registro_completo)
        assert os.path.exists(ruta_archivo)

        registro_leido = registro_service.leer_registro(propietario)
        
        assert registro_leido is not None
        assert registro_leido.get_propietario() == propietario
        assert registro_leido.get_tierra().get_superficie() == 1000.0
    finally:
        # Limpieza final
        if os.path.exists(ruta_archivo):
            os.remove(ruta_archivo)

def test_leer_registro_no_existente(registro_service: RegistroForestalService):
    """Prueba que se lanza PersistenciaException si el archivo de registro no existe."""
    with pytest.raises(PersistenciaException) as excinfo:
        registro_service.leer_registro("PropietarioFantasma")
    # Comprobamos que el error original sea FileNotFoundError
    assert isinstance(excinfo.value.error_original, FileNotFoundError)

def test_leer_registro_propietario_vacio_lanza_excepcion(registro_service: RegistroForestalService):
    """Prueba que se lanza una excepción si el nombre del propietario está vacío."""
    # El servicio no valida el string vacío, pero la operación de archivo falla,
    # lo que resulta en una PersistenciaException.
    with pytest.raises(PersistenciaException):
        registro_service.leer_registro("")
