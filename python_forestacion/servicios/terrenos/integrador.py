"""
Archivo integrador generado automaticamente
Directorio: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/servicios/terrenos
Fecha: 2025-10-21 18:14:55
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/servicios/terrenos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: plantacion_service.py
# Ruta: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/servicios/terrenos/plantacion_service.py
# ================================================================================

from typing import TYPE_CHECKING
from datetime import date
from collections import defaultdict

from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.constantes import AGUA_CONSUMIDA_RIEGO

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion

class PlantacionService:
    """
    Servicio para la lógica de negocio de la Plantación.
    """
    def plantar(self, plantacion: 'Plantacion', especie: str, cantidad: int) -> None:
        """
        Planta una cantidad de una especie de cultivo en la plantación.

        Args:
            plantacion: La plantación donde se plantará.
            especie: La especie a plantar.
            cantidad: El número de cultivos a plantar.

        Raises:
            SuperficieInsuficienteException: Si no hay espacio suficiente.
        """
        # Usamos la factory para crear un cultivo temporal y obtener su superficie
        cultivo_temporal = CultivoFactory.crear_cultivo(especie)
        superficie_requerida = cultivo_temporal.get_superficie() * cantidad

        if superficie_requerida > plantacion.get_superficie_disponible():
            raise SuperficieInsuficienteException(
                superficie_requerida=superficie_requerida,
                superficie_disponible=plantacion.get_superficie_disponible()
            )

        for _ in range(cantidad):
            nuevo_cultivo = CultivoFactory.crear_cultivo(especie)
            plantacion.agregar_cultivo(nuevo_cultivo)
        
        nueva_superficie_disponible = plantacion.get_superficie_disponible() - superficie_requerida
        plantacion.set_superficie_disponible(nueva_superficie_disponible)

        print(f"Se plantaron {cantidad} unidades de {especie}.")

    def regar(self, plantacion: 'Plantacion', fecha: date, temperatura: float, humedad: float) -> None:
        """
        Riega todos los cultivos de la plantación y muestra un resumen de la absorción.

        Raises:
            AguaAgotadaException: Si no hay suficiente agua en la plantación.
        """
        if plantacion.get_agua_disponible() < AGUA_CONSUMIDA_RIEGO:
            raise AguaAgotadaException(
                agua_requerida=AGUA_CONSUMIDA_RIEGO,
                agua_disponible=plantacion.get_agua_disponible()
            )
        
        plantacion.set_agua_disponible(plantacion.get_agua_disponible() - AGUA_CONSUMIDA_RIEGO)
        print(f"Regando la plantación... (se consumen {AGUA_CONSUMIDA_RIEGO}L de agua)")

        registry = CultivoServiceRegistry.get_instance()
        
        # Agrupa la absorción por tipo de cultivo
        absorcion_por_tipo = defaultdict(lambda: {'cantidad': 0, 'total_absorbido': 0})
        
        for cultivo in plantacion.get_cultivos():
            agua_absorbida = registry.absorber_agua(cultivo, fecha, temperatura, humedad)
            tipo = type(cultivo).__name__
            resumen = absorcion_por_tipo[tipo]
            resumen['cantidad'] += 1
            resumen['total_absorbido'] += agua_absorbida

        # Imprime el resumen
        for tipo, resumen in absorcion_por_tipo.items():
            # La absorción individual es el total absorbido dividido por la cantidad de plantas
            absorcion_individual = resumen['total_absorbido'] / resumen['cantidad']
            print(f"  - {resumen['cantidad']}x {tipo} absorbieron {absorcion_individual:.0f}L cada uno (Total: {resumen['total_absorbido']}L).")

    def mostrar_datos(self, plantacion: 'Plantacion') -> None:
        """Muestra los datos de una entidad Plantacion."""
        print(f"\n--- Datos de la Plantación ---")
        print(f"Superficie Total: {plantacion.get_superficie_total()} m²")
        print(f"Superficie Disponible: {plantacion.get_superficie_disponible():.2f} m²")
        print(f"Agua Disponible: {plantacion.get_agua_disponible()} L")
        print(f"Número de Cultivos: {len(plantacion.get_cultivos())}")
        print(f"Número de Trabajadores: {len(plantacion.get_trabajadores())}")


# ================================================================================
# ARCHIVO 3/4: registro_forestal_service.py
# Ruta: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/servicios/terrenos/registro_forestal_service.py
# ================================================================================

import os
import pickle
from typing import TYPE_CHECKING

from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.excepciones.persistencia_exception import PersistenciaException
from python_forestacion.constantes import DIRECTORIO_DATA

if TYPE_CHECKING:
    from python_forestacion.servicios.terrenos.tierra_service import TierraService
    from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService

class RegistroForestalService:
    """
    Servicio para la lógica de negocio de alto nivel del Registro Forestal,
    incluyendo la creación y la persistencia.
    """
    def crear_registro(self, propietario: str, codigo_catastral: str, sup_tierra: float, sup_plantacion: float) -> RegistroForestal:
        """
        Crea una instancia completa de un RegistroForestal.
        """
        if sup_plantacion > sup_tierra:
            raise ValueError("La superficie de la plantación no puede ser mayor a la de la tierra.")
        
        tierra = Tierra(codigo_catastral, propietario, sup_tierra)
        plantacion = Plantacion(sup_plantacion)
        registro = RegistroForestal(propietario, tierra, plantacion)
        return registro

    def persistir_registro(self, registro: RegistroForestal) -> None:
        """
        Guarda un objeto RegistroForestal en un archivo usando pickle.
        El nombre del archivo es el nombre del propietario.
        """
        if not os.path.exists(DIRECTORIO_DATA):
            os.makedirs(DIRECTORIO_DATA)
            
        nombre_archivo = os.path.join(DIRECTORIO_DATA, f"{registro.get_propietario()}.dat")
        
        try:
            with open(nombre_archivo, 'wb') as f:
                pickle.dump(registro, f)
            print(f"Registro de '{registro.get_propietario()}' guardado exitosamente en {nombre_archivo}")
        except IOError as e:
            raise PersistenciaException(operacion="guardado", error_original=e)

    @staticmethod
    def leer_registro(propietario: str) -> RegistroForestal:
        """
        Carga un objeto RegistroForestal desde un archivo.
        """
        nombre_archivo = os.path.join(DIRECTORIO_DATA, f"{propietario}.dat")
        try:
            with open(nombre_archivo, 'rb') as f:
                registro = pickle.load(f)
                print(f"Registro de '{propietario}' cargado exitosamente.")
                return registro
        except FileNotFoundError:
            raise PersistenciaException(operacion="lectura", error_original=FileNotFoundError(f"No se encontró el archivo {nombre_archivo}"))
        except (IOError, pickle.UnpicklingError) as e:
            raise PersistenciaException(operacion="lectura", error_original=e)

    def mostrar_datos(self, registro: RegistroForestal, tierra_service: 'TierraService', plantacion_service: 'PlantacionService') -> None:
        """Muestra los datos completos del registro forestal."""
        print(f"\n============== REGISTRO FORESTAL DE: {registro.get_propietario().upper()} ===============")
        tierra_service.mostrar_datos(registro.get_tierra())
        plantacion_service.mostrar_datos(registro.get_plantacion())
        print("======================================================================")


# ================================================================================
# ARCHIVO 4/4: tierra_service.py
# Ruta: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/servicios/terrenos/tierra_service.py
# ================================================================================

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.tierra import Tierra

class TierraService:
    """
    Servicio para la lógica de negocio relacionada con la Tierra.
    """
    def mostrar_datos(self, tierra: 'Tierra') -> None:
        """Muestra los datos de una entidad Tierra."""
        print(f"--- Datos de la Tierra ---")
        print(f"Propietario: {tierra.get_propietario()}")
        print(f"Código Catastral: {tierra.get_codigo_catastral()}")
        print(f"Superficie: {tierra.get_superficie()} m²")


