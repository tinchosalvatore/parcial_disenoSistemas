from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.cultivos.pino import Pino
    from python_forestacion.entidades.cultivos.olivo import Olivo
    from python_forestacion.entidades.cultivos.lechuga import Lechuga
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria

class CultivoFactory:
    """
    Implementación del patrón Factory Method para la creación de cultivos.
    Centraliza la lógica de instanciación de los diferentes tipos de cultivo.
    """

    @staticmethod
    def _crear_pino() -> 'Pino':
        from python_forestacion.entidades.cultivos.pino import Pino
        return Pino(variedad="Parana")

    @staticmethod
    def _crear_olivo() -> 'Olivo':
        from python_forestacion.entidades.cultivos.olivo import Olivo
        return Olivo(produce_aceitunas=True)

    @staticmethod
    def _crear_lechuga() -> 'Lechuga':
        from python_forestacion.entidades.cultivos.lechuga import Lechuga
        return Lechuga(tipo_hoja="Rizada")

    @staticmethod
    def _crear_zanahoria() -> 'Zanahoria':
        from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
        return Zanahoria(color="Naranja")

    @staticmethod
    def crear_cultivo(especie: str) -> 'Cultivo':
        """
        Método fábrica principal. Crea una instancia de un cultivo basado en la especie.

        Args:
            especie: El nombre de la especie a crear (ej: 'Pino').

        Returns:
            Una instancia del cultivo solicitado.

        Raises:
            ValueError: Si la especie es desconocida.
        """
        factories = {
            "Pino": CultivoFactory._crear_pino,
            "Olivo": CultivoFactory._crear_olivo,
            "Lechuga": CultivoFactory._crear_lechuga,
            "Zanahoria": CultivoFactory._crear_zanahoria
        }
        
        if especie not in factories:
            raise ValueError(f"Especie de cultivo desconocida: {especie}")
        
        return factories[especie]()
