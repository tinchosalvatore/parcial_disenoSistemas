import threading
import time
import random

from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import INTERVALO_SENSOR_TEMPERATURA

class TemperaturaReaderTask(threading.Thread, Observable[float]):
    """
    Tarea que se ejecuta en un hilo para leer la temperatura simulada.
    Es un Observable que notifica a sus observadores con cada nueva lectura.
    """
    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def _leer_temperatura(self) -> float:
        """Simula la lectura de un sensor de temperatura."""
        return round(random.uniform(5.0, 35.0), 2)

    def run(self) -> None:
        """Punto de entrada del hilo. Lee y notifica la temperatura periódicamente."""
        while not self._detenido.is_set():
            try:
                temp = self._leer_temperatura()
                print(f"[Sensor Temperatura] Nueva lectura: {temp}°C")
                self.notificar_observadores(temp)
                time.sleep(INTERVALO_SENSOR_TEMPERATURA)
            except Exception as e:
                print(f"[Sensor Temperatura] Error: {e}")

    def detener(self) -> None:
        """Señaliza al hilo que debe detenerse."""
        self._detenido.set()
