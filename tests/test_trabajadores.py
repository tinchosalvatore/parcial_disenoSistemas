import pytest
from datetime import date, timedelta
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.personal.herramienta import Herramienta
from python_forestacion.entidades.personal.apto_medico import AptoMedico
from python_forestacion.servicios.personal.trabajador_service import TrabajadorService

@pytest.fixture
def trabajador_service() -> TrabajadorService:
    return TrabajadorService()

@pytest.fixture
def herramienta_pala() -> Herramienta:
    return Herramienta(nombre="Pala", tipo="Manual")

@pytest.fixture
def tareas_simples() -> list[Tarea]:
    # El constructor de Tarea no lleva ID, se autogenera
    return [
        Tarea(descripcion="Desmalezar", duracion_horas=4),
        Tarea(descripcion="Abonar", duracion_horas=2),
    ]

def test_trabajador_con_apto_puede_trabajar(
    trabajador_service: TrabajadorService, 
    trabajador_default: Trabajador, 
    tareas_simples: list[Tarea],
    herramienta_pala: Herramienta
):
    """Prueba que un trabajador con apto médico válido puede trabajar."""
    apto_valido = AptoMedico(
        fecha_emision=date.today(),
        fecha_vencimiento=date.today() + timedelta(days=365),
        es_apto=True
    )
    # El servicio espera el objeto AptoMedico, no booleanos
    trabajador_service.asignar_apto_medico(trabajador_default, apto_valido)
    
    for tarea in tareas_simples:
        trabajador_default.asignar_tarea(tarea)

    resultado = trabajador_service.trabajar(trabajador_default, date.today(), herramienta_pala)
    
    assert resultado is True

def test_trabajador_sin_apto_no_puede_trabajar(
    trabajador_service: TrabajadorService, 
    trabajador_default: Trabajador, 
    tareas_simples: list[Tarea],
    herramienta_pala: Herramienta
):
    """Prueba que un trabajador sin apto médico no puede trabajar."""
    # No asignamos apto médico
    for tarea in tareas_simples:
        trabajador_default.asignar_tarea(tarea)

    resultado = trabajador_service.trabajar(trabajador_default, date.today(), herramienta_pala)
    
    assert resultado is False

def test_trabajador_con_apto_no_valido_no_puede_trabajar(
    trabajador_service: TrabajadorService, 
    trabajador_default: Trabajador, 
    tareas_simples: list[Tarea],
    herramienta_pala: Herramienta
):
    """Prueba que un trabajador con un apto médico 'no apto' no puede trabajar."""
    apto_no_valido = AptoMedico(
        fecha_emision=date.today(),
        fecha_vencimiento=date.today() + timedelta(days=365),
        es_apto=False  # Marcado como no apto
    )
    trabajador_service.asignar_apto_medico(trabajador_default, apto_no_valido)

    for tarea in tareas_simples:
        trabajador_default.asignar_tarea(tarea)

    resultado = trabajador_service.trabajar(trabajador_default, date.today(), herramienta_pala)
    
    assert resultado is False

def test_trabajador_con_apto_vencido_no_puede_trabajar(
    trabajador_service: TrabajadorService, 
    trabajador_default: Trabajador, 
    tareas_simples: list[Tarea],
    herramienta_pala: Herramienta
):
    """Prueba que un trabajador con un apto médico vencido no puede trabajar."""
    apto_vencido = AptoMedico(
        fecha_emision=date.today() - timedelta(days=366),
        fecha_vencimiento=date.today() - timedelta(days=1), # Venció ayer
        es_apto=True
    )
    trabajador_service.asignar_apto_medico(trabajador_default, apto_vencido)

    for tarea in tareas_simples:
        trabajador_default.asignar_tarea(tarea)

    resultado = trabajador_service.trabajar(trabajador_default, date.today(), herramienta_pala)
    
    assert resultado is False
