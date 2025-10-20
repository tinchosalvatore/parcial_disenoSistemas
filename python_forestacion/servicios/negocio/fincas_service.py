from typing import List, Dict, Type, TYPE_CHECKING
from collections import defaultdict

from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.servicios.negocio.paquete import Paquete
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.constantes import (
    AGUA_CONSUMIDA_FUMIGACION,
    COSECHA_PINO, COSECHA_OLIVO, COSECHA_LECHUGA, COSECHA_ZANAHORIA,
    PESO_PAQUETE_PINO, PESO_PAQUETE_OLIVO, PESO_PAQUETE_LECHUGA, PESO_PAQUETE_ZANAHORIA
)

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class FincasService:
    """
    Servicio de alto nivel para operaciones de negocio que involucran la finca.
    """
    def fumigar(self, plantacion: 'Plantacion') -> None:
        """Fumiga todos los cultivos, consumiendo agua por cada uno."""
        agua_requerida = len(plantacion.get_cultivos()) * AGUA_CONSUMIDA_FUMIGACION
        if plantacion.get_agua_disponible() < agua_requerida:
            raise AguaAgotadaException(agua_requerida, plantacion.get_agua_disponible())
        
        plantacion.set_agua_disponible(plantacion.get_agua_disponible() - agua_requerida)
        print(f"Se fumigaron {len(plantacion.get_cultivos())} cultivos (consumo total: {agua_requerida}L de agua).")

    def cosechar_y_empaquetar(self, plantacion: 'Plantacion') -> List[Paquete]:
        """Cosecha todos los cultivos y los empaqueta."""
        rendimiento_por_cultivo: Dict[Type['Cultivo'], int] = {
            Pino: COSECHA_PINO,
            Olivo: COSECHA_OLIVO,
            Lechuga: COSECHA_LECHUGA,
            Zanahoria: COSECHA_ZANAHORIA,
        }

        peso_paquete_por_cultivo: Dict[Type['Cultivo'], float] = {
            Pino: PESO_PAQUETE_PINO,
            Olivo: PESO_PAQUETE_OLIVO,
            Lechuga: PESO_PAQUETE_LECHUGA,
            Zanahoria: PESO_PAQUETE_ZANAHORIA,
        }

        # Calcula el rendimiento total por tipo de cultivo
        cosecha_total: Dict[Type['Cultivo'], int] = defaultdict(int)
        for cultivo in plantacion.get_cultivos():
            tipo_cultivo = type(cultivo)
            if tipo_cultivo in rendimiento_por_cultivo:
                cosecha_total[tipo_cultivo] += rendimiento_por_cultivo[tipo_cultivo]

        # Empaqueta la cosecha
        paquetes_finales: List[Paquete] = []
        for tipo_cultivo, total_kg in cosecha_total.items():
            nombre_cultivo = tipo_cultivo.__name__
            peso_paquete = peso_paquete_por_cultivo[tipo_cultivo]
            num_paquetes = total_kg // peso_paquete

            print(f"Cosecha de {nombre_cultivo}: {total_kg}kg -> {num_paquetes} paquetes de {peso_paquete}kg.")

            for _ in range(int(num_paquetes)):
                paquete = Paquete(nombre_cultivo, peso_paquete)
                # En una simulación real, aquí se agregarían los items cosechados
                # Para simplificar, creamos paquetes vacíos con el peso correcto.
                paquetes_finales.append(paquete)
        
        return paquetes_finales
