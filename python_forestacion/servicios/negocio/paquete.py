from typing import Generic, TypeVar, List

T = TypeVar('T')

class Paquete(Generic[T]):
    """
    Clase genérica que representa un paquete de un tipo de producto cosechado.
    """
    def __init__(self, tipo_producto: str, peso_por_unidad: float):
        self._tipo_producto = tipo_producto
        self._peso_por_unidad = peso_por_unidad
        self._items: List[T] = []
        self._peso_total = 0.0

    def agregar_item(self, item: T) -> None:
        self._items.append(item)
        self._peso_total += self._peso_por_unidad

    def get_tipo_producto(self) -> str:
        return self._tipo_producto

    def get_peso_total(self) -> float:
        return self._peso_total

    def get_cantidad_items(self) -> int:
        return len(self._items)
