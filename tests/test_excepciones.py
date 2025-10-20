import pytest
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.excepciones.persistencia_exception import PersistenciaException

def test_superficie_insuficiente_exception():
    """Verifica los atributos y mensajes de SuperficieInsuficienteException."""
    ex = SuperficieInsuficienteException(superficie_requerida=100.0, superficie_disponible=50.0)
    
    assert ex.superficie_requerida == 100.0
    assert ex.superficie_disponible == 50.0
    assert "Se requieren 100.00m² pero solo hay 50.00m² disponibles" in ex.get_user_message()
    assert "Superficie requerida (100.0) > disponible (50.0)" in ex.get_tech_message()

def test_agua_agotada_exception():
    """Verifica los atributos de AguaAgotadaException."""
    ex = AguaAgotadaException(agua_requerida=20.0, agua_disponible=10.0)
    
    assert ex.agua_requerida == 20.0
    assert ex.agua_disponible == 10.0
    assert "Se requieren 20.00L pero solo hay 10.00L disponibles" in ex.get_user_message()

def test_persistencia_exception():
    """Verifica los atributos de PersistenciaException."""
    original_error = ValueError("Disco lleno")
    ex = PersistenciaException(operacion="guardado", error_original=original_error)
    
    assert ex.operacion == "guardado"
    assert ex.error_original is original_error
    assert "Ocurrió un error durante la operación de guardado" in ex.get_user_message()
    assert "Error en guardado: Disco lleno" in ex.get_tech_message()
