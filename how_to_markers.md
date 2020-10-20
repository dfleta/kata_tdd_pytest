
## Working with custom markers
### Marking test functions and selecting them for a run
https://docs.pytest.org/en/latest/example/markers.html#mark-examples

Dividir el código en directorio `src` y `test`

En cada uno de esos dos directorios situar un fichero `__init__.py` vacío para indicar que son módulos (sic)

#### Registering markers for your test suite is simple
En el raíz del proyecto, situar el fichero `pytest.ini` y escribir nombre del marker y su descripción (opcional) tras los `:`

    [pytest]
        markers = 
        division_cero: coeficiente a es 0


En cada fichero `test_xxx.py` importar `pytest` para utilizar los decoradores `@pytest.mark` 

```python
import pytest

@pytest.mark.division_cero
def test_division_por_cero():
    assert raiz_ecuacion_segundo_grado(0, 1, 1) == None
```

Seleccionar el test o `marker`:

```bash
$ pytest -v -m "division_cero"
==================================== test session starts ===============================
platform linux -- Python 3.6.9, pytest-6.1.1, py-1.9.0, pluggy-0.13.1 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/david/Escritorio/Programacion/codigo/square_test, configfile: pytest.ini
collected 3 items / 2 deselected / 1 selected                                                                      

test/square_root_test.py::test_division_por_cero PASSED                                                      [100%]

================== 1 passed, 2 deselected in 0.01s ======================
# observar que sólo ha seleccionado 1
```