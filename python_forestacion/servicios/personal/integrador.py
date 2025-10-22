"""
Archivo integrador generado automaticamente
Directorio: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/servicios/personal
Fecha: 2025-10-21 21:58:15
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/servicios/personal/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: trabajador_service.py
# Ruta: /home/martinsalvatore/repos/python/diseño/parcial/parcial_disenoSistemas/python_forestacion/servicios/personal/trabajador_service.py
# ================================================================================

from datetime import date
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from python_forestacion.entidades.personal.trabajador import Trabajador
    from python_forestacion.entidades.personal.apto_medico import AptoMedico
    from python_forestacion.entidades.personal.tarea import Tarea
    from python_forestacion.entidades.personal.herramienta import Herramienta

class TrabajadorService:
    """
    Servicio para la lógica de negocio relacionada con los Trabajadores.
    """
    def asignar_apto_medico(self, trabajador: 'Trabajador', apto: 'AptoMedico') -> None:
        trabajador.set_apto_medico(apto)
        print(f"Se asignó un apto médico a {trabajador.get_nombre_completo()}.")

    def trabajar(self, trabajador: 'Trabajador', fecha_actual: date, herramienta: 'Herramienta') -> bool:
        """
        Simula a un trabajador realizando sus tareas en un día.
        Verifica si el trabajador tiene un apto médico vigente.
        """
        apto = trabajador.get_apto_medico()
        if apto is None or not apto.es_apto() or apto.esta_vencido(fecha_actual):
            print(f"{trabajador.get_nombre_completo()} no puede trabajar. Apto médico no válido o vencido.")
            return False

        print(f"{trabajador.get_nombre_completo()} está trabajando con {herramienta.get_nombre()}.")
        for tarea in trabajador.get_tareas():
            print(f"  - Realizando tarea: {tarea.get_descripcion()} (Duración: {tarea.get_duracion_horas()}h)")
        
        return True

    def _obtener_id_tarea(self, tarea: 'Tarea') -> int:
        """Función de ayuda para ordenar tareas por ID."""
        return tarea.get_id()

    def mostrar_datos(self, trabajador: 'Trabajador') -> None:
        """Muestra los datos de un trabajador."""
        print(f"\n--- Datos del Trabajador ---")
        print(f"Nombre: {trabajador.get_nombre_completo()}")
        print(f"DNI: {trabajador.get_dni()}")
        apto = trabajador.get_apto_medico()
        if apto:
            print(f"Apto Médico: {'Sí' if apto.es_apto() else 'No'} (Vence: {apto.get_fecha_vencimiento()})")
        else:
            print("Apto Médico: No asignado")
        
        tareas = trabajador.get_tareas()
        # La rúbrica prohibe lambdas, usamos un método de ayuda para ordenar
        tareas.sort(key=self._obtener_id_tarea, reverse=True)
        print(f"Tareas asignadas ({len(tareas)}): ")
        for tarea in tareas:
            print(f"  - ID: {tarea.get_id()}, Desc: {tarea.get_descripcion()}")


