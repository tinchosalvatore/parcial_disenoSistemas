import pytest
import time
from unittest.mock import MagicMock
from datetime import datetime

from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask
from python_forestacion.constantes import TEMP_MIN_RIEGO, HUMEDAD_MAX_RIEGO
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor

# Fixtures para las tareas
@pytest.fixture
def temperatura_task():
    return TemperaturaReaderTask()

@pytest.fixture
def humedad_task():
    return HumedadReaderTask()

@pytest.fixture
def control_task(plantacion_default): # Usa la plantacion de conftest
    # Mock del servicio de plantación para no depender de su lógica interna
    mock_plantacion_service = MagicMock()
    return ControlRiegoTask(mock_plantacion_service, plantacion_default)


class TestControlRiegoLogic:
    """Tests para la lógica de decisión de ControlRiegoTask, sin hilos."""

    def test_debe_regar_condiciones_optimas(self, control_task: ControlRiegoTask, temperatura_task: TemperaturaReaderTask, humedad_task: HumedadReaderTask):
        """Verifica que debe regar cuando la temperatura es alta y la humedad es baja."""
        evento_temp = EventoSensor(valor=TEMP_MIN_RIEGO + 1, fecha=datetime.now())
        evento_hum = EventoSensor(valor=HUMEDAD_MAX_RIEGO - 1, fecha=datetime.now())
        control_task.actualizar(temperatura_task, evento_temp)
        control_task.actualizar(humedad_task, evento_hum)
        assert control_task._debe_regar() is True

    def test_no_debe_regar_por_baja_temperatura(self, control_task: ControlRiegoTask, temperatura_task: TemperaturaReaderTask, humedad_task: HumedadReaderTask):
        """Verifica que no riega si la temperatura es muy baja."""
        evento_temp = EventoSensor(valor=TEMP_MIN_RIEGO - 1, fecha=datetime.now())
        evento_hum = EventoSensor(valor=HUMEDAD_MAX_RIEGO - 1, fecha=datetime.now())
        control_task.actualizar(temperatura_task, evento_temp)
        control_task.actualizar(humedad_task, evento_hum)
        assert control_task._debe_regar() is False

    def test_no_debe_regar_por_alta_humedad(self, control_task: ControlRiegoTask, temperatura_task: TemperaturaReaderTask, humedad_task: HumedadReaderTask):
        """Verifica que no riega si la humedad es muy alta."""
        evento_temp = EventoSensor(valor=TEMP_MIN_RIEGO + 1, fecha=datetime.now())
        evento_hum = EventoSensor(valor=HUMEDAD_MAX_RIEGO + 1, fecha=datetime.now())
        control_task.actualizar(temperatura_task, evento_temp)
        control_task.actualizar(humedad_task, evento_hum)
        assert control_task._debe_regar() is False

    def test_no_debe_regar_sin_datos_de_sensores(self, control_task: ControlRiegoTask):
        """Verifica que no riega si faltan datos de uno o ambos sensores."""
        assert control_task._debe_regar() is False # Sin datos
        control_task._ultima_temperatura = 25.0
        assert control_task._debe_regar() is False # Solo con temperatura
        control_task._ultima_temperatura = None
        control_task._ultima_humedad = 40.0
        assert control_task._debe_regar() is False # Solo con humedad


class TestRiegoThreading:
    """Tests para la funcionalidad de hilos y el apagado seguro."""

    def test_graceful_shutdown(self, temperatura_task, humedad_task, control_task):
        """Prueba que todos los hilos se inician y se detienen correctamente."""
        tasks = [temperatura_task, humedad_task, control_task]

        # Iniciar todos los hilos
        for task in tasks:
            task.start()
        
        # Verificar que están vivos
        time.sleep(0.1) # Dar tiempo a que los hilos arranquen
        for task in tasks:
            assert task.is_alive()

        # Detener todos los hilos
        for task in tasks:
            task.detener()
        
        # Esperar a que terminen
        for task in tasks:
            task.join(timeout=4) # Timeout para no bloquear el test indefinidamente
        
        # Verificar que ya no están vivos
        for task in tasks:
            assert not task.is_alive()
