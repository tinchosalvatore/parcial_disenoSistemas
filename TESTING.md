# Guía de Testing - PythonForestal

Este documento describe la estrategia de testing, la estructura de la suite de pruebas y cómo ejecutar los tests para el proyecto PythonForestal.

## Cobertura de Tests

El objetivo de la suite de tests es asegurar la correcta implementación de los patrones de diseño y la lógica de negocio principal. La cobertura de código actual es:

- **Cobertura Total: 84%**

Desglose por componentes principales:
- **Patrones de Diseño**: ~100%
- **Entidades**: ~85%
- **Servicios Principales**: ~75%
- **Riego Automático**: ~82%
- **Persistencia**: ~77%

*Nota: Estos valores son aproximados. Para ver el reporte detallado, ejecuta `pytest --cov=python_forestacion --cov-report=html` y abre `htmlcov/index.html`.*

---

## Estructura de Tests

La suite de tests está organizada en la carpeta `tests/` y sigue la estructura del código fuente:

```
tests/
├── __init__.py
├── conftest.py               # Fixtures globales y configuración
├── test_patrones.py          # Tests para Singleton, Factory, Observer, Strategy
├── test_cultivos.py          # Tests para las entidades de cultivo
├── test_plantacion.py        # Tests para el servicio de plantación
├── test_persistencia.py      # Tests para el guardado y lectura de datos
├── test_trabajadores.py      # Tests para el servicio de trabajadores
├── test_excepciones.py       # Tests para las excepciones personalizadas
└── test_riego.py             # Tests para el sistema de riego con threads
```

- **`conftest.py`**: Contiene fixtures reutilizables como `plantacion_default` y `trabajador_default`, además de la configuración del `sys.path` para que los tests encuentren el código de la aplicación.

---

## Ejecutar Tests

### Requisitos

Asegúrate de tener las dependencias de desarrollo instaladas:
```bash
pip install -r requirements-dev.txt
```

### Ejecutar Todos los Tests

Para ejecutar la suite completa en modo verbose:
```bash
pytest -v
```

### Ejecutar Tests por Categoría

Puedes ejecutar los tests de un archivo específico para enfocarte en un área del sistema:

```bash
# Probar solo la implementación de los patrones de diseño
pytest tests/test_patrones.py

# Probar la lógica de la plantación (plantar, regar)
pytest tests/test_plantacion.py

# Probar el sistema de riego y sus hilos
pytest tests/test_riego.py

# Probar la persistencia de datos
pytest tests/test_persistencia.py
```

### Filtrar Tests por Nombre

Usa la opción `-k` para ejecutar tests que coincidan con una expresión.

```bash
# Ejecutar solo los tests relacionados con 'shutdown' en el archivo de riego
pytest tests/test_riego.py -k "shutdown"

# Ejecutar solo los tests relacionados con 'excepciones'
pytest -k "exception"
```

---

## Agregar Nuevos Tests

Para mantener la consistencia de la suite de pruebas, sigue estas guías al agregar nuevos tests:

1.  **Nomenclatura**: Los archivos deben llamarse `test_*.py` y las funciones de test `test_*()`.
2.  **Ubicación**: Si el test es para una nueva funcionalidad, considera si encaja en un archivo existente o si requiere un nuevo archivo `test_*.py`.
3.  **Usa Fixtures**: Revisa `conftest.py` para ver si puedes reutilizar fixtures existentes (`plantacion_default`, `trabajador_default`, etc.). Si necesitas un estado inicial complejo y repetido, considera agregar una nueva fixture.
4.  **Independencia**: Cada test debe ser independiente. No debe depender del resultado o del estado dejado por otro test.
5.  **Excepciones**: Usa `pytest.raises()` para verificar que tu código lanza las excepciones esperadas en casos de error.

**Ejemplo de un nuevo test:**
```python
# En el archivo tests/test_cultivos.py

def test_nueva_caracteristica_cultivo(pino_test: Pino):
    """Verifica la nueva característica X del cultivo."""
    # 1. Preparación (Arrange)
    valor_inicial = pino_test.get_alguna_propiedad()
    
    # 2. Acción (Act)
    pino_test.hacer_algo()
    
    # 3. Verificación (Assert)
    assert pino_test.get_alguna_propiedad() != valor_inicial
```
