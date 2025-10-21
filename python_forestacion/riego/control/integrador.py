"""
Archivo integrador generado automaticamente
Directorio: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/riego/control
Fecha: 2025-10-21 18:14:55
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/riego/control/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: control_riego_task.py
# Ruta: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/riego/control/control_riego_task.py
# ================================================================================

import threading
import time
from datetime import date
from typing import Optional, TYPE_CHECKING

from python_forestacion.patrones.observer.observer import Observer
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor
from python_forestacion.constantes import (
    TEMP_MIN_RIEGO,
    HUMEDAD_MAX_RIEGO,
    INTERVALO_CONTROL_RIEGO
)

if TYPE_CHECKING:
    from python_forestacion.patrones.observer.observable import Observable
    from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
    from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
    from python_forestacion.entidades.terrenos.plantacion import Plantacion
    from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService

class ControlRiegoTask(threading.Thread, Observer[EventoSensor]):
    """
    Tarea que se ejecuta en un hilo para controlar el sistema de riego.
    Es un Observer de los sensores de temperatura y humedad.
    """
    def __init__(self, plantacion_service: 'PlantacionService', plantacion: 'Plantacion'):
        threading.Thread.__init__(self, daemon=True)
        self._plantacion_service = plantacion_service
        self._plantacion = plantacion
        self._ultima_temperatura: Optional[float] = None
        self._ultima_humedad: Optional[float] = None
        self._detenido = threading.Event()

    def actualizar(self, observable: 'Observable', evento: EventoSensor) -> None:
        """
        Recibe notificaciones de los sensores y actualiza los valores internos.
        Distingue la fuente del evento gracias al parámetro 'observable'.
        """
        from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
        from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask

        if isinstance(observable, TemperaturaReaderTask):
            self._ultima_temperatura = evento.valor
        elif isinstance(observable, HumedadReaderTask):
            self._ultima_humedad = evento.valor

    def _debe_regar(self) -> bool:
        """Comprueba si se cumplen las condiciones para el riego."""
        if self._ultima_temperatura is None or self._ultima_humedad is None:
            return False
        
        return (
            self._ultima_temperatura > TEMP_MIN_RIEGO and 
            self._ultima_humedad < HUMEDAD_MAX_RIEGO
        )

    def run(self) -> None:
        """Punto de entrada del hilo. Comprueba y ejecuta el riego periódicamente."""
        while not self._detenido.is_set():
            try:
                if self._debe_regar():
                    print(f"[Control Riego] Condiciones óptimas (Temp: {self._ultima_temperatura}°C, Humedad: {self._ultima_humedad}%). Iniciando riego.")
                    try:
                        self._plantacion_service.regar(
                            self._plantacion, 
                            date.today(), 
                            self._ultima_temperatura, 
                            self._ultima_humedad
                        )
                    except Exception as e:
                        print(f"[Control Riego] Error al intentar regar: {e}")
                else:
                    print(f"[Control Riego] Condiciones no aptas para riego (Temp: {self._ultima_temperatura}°C, Humedad: {self._ultima_humedad}%).")
                
                time.sleep(INTERVALO_CONTROL_RIEGO)
            except Exception as e:
                print(f"[Control Riego] Error: {e}")

    def detener(self) -> None:
        """Señaliza al hilo que debe detenerse."""
        self._detenido.set()


