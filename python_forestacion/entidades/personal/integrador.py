"""
Archivo integrador generado automaticamente
Directorio: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/entidades/personal
Fecha: 2025-10-21 18:14:55
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/entidades/personal/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/5: apto_medico.py
# Ruta: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/entidades/personal/apto_medico.py
# ================================================================================

from datetime import date

class AptoMedico:
    """
    Representa el certificado de aptitud médica de un trabajador.
    """
    def __init__(self, fecha_emision: date, fecha_vencimiento: date, es_apto: bool):
        """
        Inicializa el apto médico.

        Args:
            fecha_emision: Fecha de emisión del certificado.
            fecha_vencimiento: Fecha de vencimiento del certificado.
            es_apto: True si el trabajador está apto.
        """
        if fecha_vencimiento < fecha_emision:
            raise ValueError("La fecha de vencimiento no puede ser anterior a la de emisión.")

        self._fecha_emision = fecha_emision
        self._fecha_vencimiento = fecha_vencimiento
        self._es_apto = es_apto

    def get_fecha_emision(self) -> date:
        return self._fecha_emision

    def get_fecha_vencimiento(self) -> date:
        return self._fecha_vencimiento

    def es_apto(self) -> bool:
        return self._es_apto

    def esta_vencido(self, fecha_actual: date) -> bool:
        """Verifica si el apto médico está vencido en la fecha actual."""
        return fecha_actual > self._fecha_vencimiento


# ================================================================================
# ARCHIVO 3/5: herramienta.py
# Ruta: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/entidades/personal/herramienta.py
# ================================================================================

class Herramienta:
    """
    Representa una herramienta que un trabajador puede utilizar.
    """
    def __init__(self, nombre: str, tipo: str):
        """
        Inicializa la herramienta.

        Args:
            nombre: El nombre de la herramienta (ej: 'Pala').
            tipo: El tipo de herramienta (ej: 'Manual', 'Maquinaria').
        No pueden estar vacíos
        """
        if not nombre or not tipo:
            raise ValueError("El nombre y el tipo no pueden estar vacíos.")
        
        self._nombre = nombre
        self._tipo = tipo

    def get_nombre(self) -> str:
        return self._nombre

    def get_tipo(self) -> str:
        return self._tipo


# ================================================================================
# ARCHIVO 4/5: tarea.py
# Ruta: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/entidades/personal/tarea.py
# ================================================================================

from threading import Lock

class Tarea:
    """
    Representa una tarea que puede ser asignada a un trabajador.
    """
    _next_id = 1
    _lock = Lock()  # para el manejo de concurrencia de los Hilos

    def __init__(self, descripcion: str, duracion_horas: int):
        """
        Inicializa una tarea.

        Args:
            descripcion: Descripción de la tarea (ej: 'Regar').
            duracion_horas: Duración estimada en horas.
        """
        with Tarea._lock:
            self._id = Tarea._next_id
            Tarea._next_id += 1
        
        self._descripcion = descripcion
        self._duracion_horas = duracion_horas

    def get_id(self) -> int:
        return self._id

    def get_descripcion(self) -> str:
        return self._descripcion

    def get_duracion_horas(self) -> int:
        return self._duracion_horas


# ================================================================================
# ARCHIVO 5/5: trabajador.py
# Ruta: /home/martinsalvatore/repos/python/clases_del_java/parcial/parcial_disenoSistemas/python_forestacion/entidades/personal/trabajador.py
# ================================================================================

from typing import List, Optional, TYPE_CHECKING

# evita importaciones circulares, ya que es False durante tiempo de ejecucion, pero True durante el chequeo de
# tipos como Optional[AptoMedico] o List[Tarea]
if TYPE_CHECKING:
    from python_forestacion.entidades.personal.apto_medico import AptoMedico
    from python_forestacion.entidades.personal.tarea import Tarea

class Trabajador:
    """
    Representa a un trabajador de la plantación.
    """
    def __init__(self, nombre: str, apellido: str, dni: str):
        """
        Inicializa un trabajador.

        Args:
            nombre: Nombre del trabajador.
            apellido: Apellido del trabajador.
            dni: DNI del trabajador.
        """
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._apto_medico: Optional['AptoMedico'] = None
        self._tareas: List['Tarea'] = []

    def get_nombre_completo(self) -> str:
        return f"{self._nombre} {self._apellido}"

    def get_dni(self) -> str:
        return self._dni

    def get_apto_medico(self) -> Optional['AptoMedico']:
        return self._apto_medico

    def set_apto_medico(self, apto: Optional['AptoMedico']) -> None:
        self._apto_medico = apto

    def get_tareas(self) -> List['Tarea']:
        """Retorna una copia de la lista de tareas."""
        return self._tareas.copy()

    def asignar_tarea(self, tarea: 'Tarea') -> None:
        self._tareas.append(tarea)


