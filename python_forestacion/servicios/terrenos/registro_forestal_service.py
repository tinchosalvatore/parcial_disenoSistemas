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
