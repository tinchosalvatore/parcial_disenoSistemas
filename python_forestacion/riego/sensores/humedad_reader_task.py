import threading
import time
import random
from datetime import datetime

from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import INTERVALO_SENSOR_HUMEDAD
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor

class HumedadReaderTask(threading.Thread, Observable[EventoSensor]):
    """
    Tarea que se ejecuta en un hilo para leer la humedad simulada.
    Es un Observable que notifica a sus observadores con cada nueva lectura.
    """
    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def _leer_humedad(self) -> float:
        """Simula la lectura de un sensor de humedad."""
        return round(random.uniform(20.0, 80.0), 2)

    def run(self) -> None:
        """Punto de entrada del hilo. Lee y notifica la humedad periódicamente."""
        while not self._detenido.is_set():
            try:
                humedad = self._leer_humedad()
                print(f"[Sensor Humedad] Nueva lectura: {humedad}%")
                evento = EventoSensor(valor=humedad, fecha=datetime.now())
                self.notificar_observadores(evento)
                time.sleep(INTERVALO_SENSOR_HUMEDAD)
            except Exception as e:
                print(f"[Sensor Humedad] Error: {e}")

    def detener(self) -> None:
        """Señaliza al hilo que debe detenerse."""
        self._detenido.set()
