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
