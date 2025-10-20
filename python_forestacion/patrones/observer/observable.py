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
