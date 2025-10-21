"""
Archivo integrador generado automaticamente
Directorio: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/patrones/observer
Fecha: 2025-10-21 18:14:55
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/patrones/observer/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: observable.py
# Ruta: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/patrones/observer/observable.py
# ================================================================================

from abc import ABC
from typing import Generic, List, TypeVar

from python_forestacion.patrones.observer.observer import Observer

T = TypeVar('T')

class Observable(Generic[T], ABC):
    """
    La clase base Observable (publicador) del patrón Observer.
    Mantiene una lista de observadores y los notifica de los cambios.
    """
    def __init__(self):
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        """Agrega un observador a la lista si no está ya presente."""
        if observador not in self._observadores:
            self._observadores.append(observador)

    def remover_observador(self, observador: Observer[T]) -> None:
        """Remueve un observador de la lista."""
        self._observadores.remove(observador)

    def notificar_observadores(self, evento: T) -> None:
        """Notifica a todos los observadores enviándoles el evento."""
        for observador in self._observadores:
            observador.actualizar(self, evento)


# ================================================================================
# ARCHIVO 3/3: observer.py
# Ruta: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/patrones/observer/observer.py
# ================================================================================

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.patrones.observer.observable import Observable

T = TypeVar('T')

class Observer(Generic[T], ABC):
    """
    La interfaz Observer (suscriptor) del patrón Observer.
    Define el método actualizar que será llamado por el Observable.
    """
    @abstractmethod
    def actualizar(self, observable: 'Observable', evento: T) -> None:
        """
        Recibe una actualización del observable.

        Args:
            observable: La instancia del observable que notifica el evento.
            evento: El dato o evento notificado por el observable.
        """
        pass


