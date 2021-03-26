# Kata TDD con Pytest y markers

Cómo utilizar `pytest.ini`y los `markers` para configurar los casos test.


## Trabajar con custom markers

### Marking test functions y seleccionarlas para ejecutarse

https://docs.pytest.org/en/latest/example/markers.html#mark-examples

Separar el código en directorios `src` y `test`

En cada uno de esos dos directorios situar un fichero `__init__.py` vacío para indicar que son módulos (sic)

### Registrar markers para cada test en la suite

En el raíz del proyecto, situar el fichero `pytest.ini` y escribir nombre del marker y su descripción (opcional) tras los `:`

```ini
    [pytest]
        markers = 
        division_cero: coeficiente a es 0
```

En cada módulo /fichero correspondiente a los test de cada módulo `test_xxx.py` importar `pytest` para utilizar los decoradores `@pytest.mark` 

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

Una vez creados los `markers` y registrados en `pytest.ini` , obtenemos una lista de ellos:

`$ pytest --markers`

## TOX

![Tox flow](./tox_flow.png)


Workflow de Tox:

https://tox.readthedocs.io/en/latest/index.html

Paso a paso aquí:

https://tox.readthedocs.io/en/latest/example/basic.html


1. Creamos un entorno virtual, lo activamos y chequeamos las dependencias que se instalan:

    ```bash
    $ python3.6 -m venv venv
    $ source venv/bin/activate
    (venv) $ pip3 list
    pip (9.0.1)
    pkg-resources (0.0.0)
    setuptools (39.0.1)
    ```

2. Instalamos `pytest` y `tox` (no las `setuptools` que ya han sido instaladas al crear el entorno virtual):

    https://pip.pypa.io/en/stable/reference/pip_install/ 

    https://tox.readthedocs.io/en/latest/ 


    ```bash
    (venv) $ python3.6 -m pip install pytest
    (venv) $ python3.6 -m pip install tox

    (venv) $ pip3 list |  grep tox
    ```

3. Crear `requirements.txt`
   
   `(venv) $ pip3 freeze > requirements.txt`

4. Crear `setup.py`. 
   Usar como template este: https://github.com/dfleta/api-rest-gildedrose/blob/master/setup.py e incluir las dependencias del fichero `requirements.txt` anterior. 

   Eliminar la dependencia `pkg-resources==0.0.0` porque es un bug de pip.
   
5. Crear un fichero `tox.ini` con la configuración en la raíz del proyecto:

    ```ini
    # content of: tox.ini , put in same dir as setup.py
    [tox]
    envlist = py36
    # los interpretes a utilizar han de estar instalados en la máquina
    [testenv]
    # install testing framework
    # ... or install anything else you might need here
    deps = 
            -rrequirements.txt
    # run the tests
    # ... or run any other command line tool you need to run here
    commands = pytest
    ```

6. Invocar `tox`.
   
   Hace lo que promete:

    > 1. Chequea que tu paquete instala correctamente en diferentes versiones de Python e intérpretes.
    > 2. Ejecuta tus tests en cada uno de los entornos, configurando el framework para los test que elijas.
    > 3. Actúa como un frontend para servidores de Continuous Integration, "_greatly reducing boilerplate and merging CI and shell-based testing_". <== siguiente paso en esta práctica.

    Crea un directorio `.tox` bajo el cual encontramos los entornos virtuales indicados en la envlist del tox.ini (py36) y un egg de distrbución (leer más adelante);

    ```bash
    # -l 2 para bajar solo 2 niveles
    $ tree -L 2 .tox
    .tox
    ├── dist
    │   └── square root testing-0.0.1.zip
    ├── log
    │   
    └── py36
        ├── bin
        ├── lib
        ├── log
        ├── pyvenv.cfg
        └── tmp
    ```

    ``` bash
    (venv) $ tox
    # Crea el fichero de distribución a partir del setup.py
    GLOB sdist-make: /square_test/setup.py

    # Crea un entorno virtual para cada uno indicado en la envlist del tox.ini
    py36 inst-nodeps: /square_test/.tox/.tmp/package/1/square root testing-0.0.1.zip
   
    # Instala las dependencias en el entorno virtual indicadas en requirements.txt
    py36 installed: appdirs==1.4.4,attrs==20.3.0,distlib==0.3.1,filelock==3.0.12,importlib-metadata==2.1.1,importlib-resources==4.1.1,iniconfig==1.1.1,packaging==20.8,pluggy==0.13.1,py==1.10.0,pyparsing==2.4.7,pytest==6.2.1,six==1.15.0,square-root-testing 
    py36 run-test-pre: PYTHONHASHSEED='93282115'
   
    # Ejecuta los comandos de la lista commands del tox.ini
    py36 run-test: commands[0] | pytest

    ========================== test session starts =======================
    platform linux -- Python 3.6.9, pytest-6.2.1, py-1.10.0, pluggy-0.13.1
    cachedir: .tox/py36/.pytest_cache
    rootdir: /square_test, configfile: pytest.ini
    collected 6 tems                                                                                               
    test/test_ square_root.py [ 16%]
    test/test_b_c_nulo.py     [ 33%]
    test/test_c_nulo.py .     [ 66%]
    test/test_division_cero.py .. [100%]

    ========== 6 passed in 0.02s ================
    _____________summary ________________________
    py36: commands succeeded
    congratulations :)
   
    ```

Se instalan en el entorno virtual las dependencias del `requirements.txt` y todas aquellas dependendencias que indice en la sección `deps = ` del `tox.ini`  
Entiendo que se copian los ficheros de configuración de las herramientas, y los usa tox => ¿cómo se copiarían los ficheros de configuración de coverage y black al entorno virtual de prueba?


## Dist

En este artículo se explica bien qué sucede con el estándar mínimo que ha de tener un paquete, y los estándares PEP517 y PEP518, las setuptools y wheel y, sobretodo, el fichero `pyproject.toml` 

https://snarky.ca/what-the-heck-is-pyproject-toml/

La idea es usar el fichero `pyproject.toml` para ser utilizado para configurar todas las herramientas como coverage, wheels, tox, etc. 


Packaging en Tox y con otras herramientas => añadir  `pyproject.toml` con la configuración (no es necesario):

```toml
[build-system]
requires = [
    "setuptools >= 35.0.2",
    "setuptools_scm >= 2.0.0, <3"
]
build-backend = "setuptools.build_meta"
```

https://tox.readthedocs.io/en/latest/example/package.html


He decido hacerlo de este modo:

1. En `tox.ini` indico un directorio fuera de .tox donde situar el `egg.zip`:
    
    ```ini
    # content of: tox.ini
    [tox]
    envlist = py36
    # indicar un directorio fuera de .tox donde situar el zip con el egg
    distdir=./dist-egg
    ```
    La configuración de `tox.ini` (como `distdir`) está aquí:
    https://tox.readthedocs.io/en/latest/config.html

2. Tras pasar los test, empaqueto con wheel

    `(venv) $ pip3 install wheel`

    que crea un directorio `./dist` donde figura el fich `whl`

    Aquí `wheel`:

    https://wheel.readthedocs.io/en/stable/user_guide.html

    En la sección `commands` de tox.ini añadir:
    `wheel setup.py bdtis_wheel`

    Crea un directorio `dist` donde colocal el fichero wheel. 

 
El problema de esta configuración es que si un caso test falla, el empaquetado con wheel se completa de igua modo, no así el que tox crea en `.tox/dist`.


## Code formatter

Black

https://pypi.org/project/black/ 

`$ black [source_file_or_directory]`

Black code style:

https://pypi.org/project/black/ 

### Configuration format

Black usa `pyproject.toml` que es un TOML file. La ventaja de usar este fichero es que sirve de punto de configuración para muchas de las herramientas que estoy usando: coverage, tox, black.

It contains separate sections for different tools. Black is using the [tool.black] section. The option keys are the same as long names of options on the command line.

Note that you have to use single-quoted strings in TOML for regular expressions. It's the equivalent of r-strings in Python. Multiline strings are treated as verbose regular expressions by Black. Use [ ] to denote a significant space character.

Ver fichero 

```toml
[tool.black]
line-length = 88
target-version = ['py36', 'py37', 'py38']
include = '\.pyi?$'
exclude = '''
/(
    \.eggs
  | \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | \.vscode
  | _build
  | buck-out
  | build
  | dist
  | venv
  # The following are specific to Black, you probably don't want those.
  | blib2to3
  | tests/data
  | profiling
)/
'''
```

## Coverage

https://coverage.readthedocs.io/en/latest

`$ pip3 install coverage`

`$ coverage run -m pytest`

#### Data file
Coverage.py collects execution data in a file called “.coverage”

#### Sólo analizar el dir source indicado

`$ coverage run --source ./src -m pytest`

--source creo que se ve sobreescrito por la configuración exclude o include en el fichero de configuración `.coveragerc`

Como invoco coverage llamando al módulo pytest, sólo se analizan los ficheros de código que son ejecutados por los casos test.

#### Excluir líneas de código

https://coverage.readthedocs.io/en/latest/excluding.html

Ver el fichero `.coveragerc`

Puede moverse al fichero de configuración del proyecto `pyproject.toml` si se instala `coverage` de modo:

https://coverage.readthedocs.io/en/latest/config.html#config

`pip install coverage[toml]`


##### para ver el report

`$ coverage report`

Para saber qué lineas no se han ejecutado:

`$ coverage report -m`


#### Anotar el código

`$ coverage annotate -d ./coverage_annotation`

Antes has de ejecutar:

`$ coverage run --source ./src -m pytest`

Produce un texto anotado del código fuente. Con `-d` especificamos un directorio de salida para el fichero con el código anotado. Sin `-d`, los ficheros anotados son escritos en el directorio original del fichero Python.

Coverage status for each line of source is indicated with a character prefix:

    > executed
    ! missing (not executed)
    - excluded


Si seguimos este flujo de trabajo:

`$ pytest -m b_nulo`

`$ coverage run --source ./src -m pytest -m b_nulo`

`$ coverage annotate -d ./coverage_annotation`

conseguimos ver en las anotaciones del código sólo el **backward slice** del código que ha sido ejecutado para pasar el caso test del marker indicado.

Es mejor esto que el report, ya que leo si se ha cubierto el código que estoy testeando bajo ese caso test específico.

#### Echarle un ojo a la extensión pytest-cov de pytest

https://pytest-cov.readthedocs.io/en/latest/readme.html#installation


### eggs

tox crea en la carpeta .tox/dist un paquete de distribución `egg` para instalar con `easy_install`:

`square root testing-0.0.1.zip`

Contiene el código del paquete y metadatos, como los `.jar`

Ha sido superseed por wheel (convertir un egg a wheel:)

https://wheel.readthedocs.io/en/stable/quickstart.html



https://stackoverflow.com/questions/2051192/what-is-a-python-egg

    Note: Egg packaging has been superseded by Wheel packaging.

Same concept as a .jar file in Java, it is a .zip file with some metadata files renamed .egg, for distributing code as bundles.

Specifically: The Internal Structure of Python Eggs: http://svn.python.org/projects/sandbox/trunk/setuptools/doc/formats.txt

    A "Python egg" is a logical structure embodying the release of a specific version of a Python project, comprising its code, resources, and metadata. There are multiple formats that can be used to physically encode a Python egg, and others can be developed. However, a key principle of Python eggs is that they should be discoverable and importable. That is, it should be possible for a Python application to easily and efficiently find out what eggs are present on a system, and to ensure that the desired eggs' contents are importable.

    The .egg format is well-suited to distribution and the easy uninstallation or upgrades of code, since the project is essentially self-contained within a single directory or file, unmingled with any other projects' code or resources. It also makes it possible to have multiple versions of a project simultaneously installed, such that individual programs can select the versions they wish to use.


## Bandit

Es conveniente integrar en el ciclo CI cuanto antes cuestiones sobre la seguridad de las aplicaciones. De DevOps hay que evolucionar a SecDevOps.

Bandit realiza un análisis **estático**  del código en busca de vulnerabilidades:

https://pypi.org/project/bandit/

https://bandit.readthedocs.io/en/latest/config.html

```bash
# install
$ pip3 install bandit

#run
S bandit -r path/to/your/code
# Across the examples/ directory, showing three lines of context and only reporting on the high-severity issues:
$ bandit examples/*.py -n 3 -lll

# Nuesto caso:
$ bandit -r ./src/ ./test
# informa de la presencia de assert que eliminarán código cuando se ejecute en producción

$ bandit -r[main]  INFO    profile include tests: None
[main]  INFO    profile exclude tests: None
[main]  INFO    cli include tests: None
[main]  INFO    cli exclude tests: None
[main]  INFO    running on Python 3.6.9
Run started:2021-03-26 13:09:52.411873

Test results:
        No issues identified.

Code scanned:
        Total lines of code: 25
        Total lines skipped (#nosec): 0

Run metrics:
        Total issues (by severity):
                Undefined: 0.0
                Low: 0.0
                Medium: 0.0
                High: 0.0
        Total issues (by confidence):
                Undefined: 0.0
                Low: 0.0
                Medium: 0.0
                High: 0.0
Files skipped (0): ./src/
```

### Configuracion

Para generar un fichero de configuración (no es necesario):

`$ bandit-config-generator -o .bandit`

Para usarlo:

`$ bandit-c .bandit`


La lista de test que pasa bandit para chequear vulnerabilidades es esta: muy educativo para aprender las vulnerabilidades en código Python: 

https://bandit.readthedocs.io/en/latest/plugins/index.html#complete-test-plugin-listing

En el archivo de configuración se pueden excluir los casos test por su etiqueta.

### Actualizar tox.ini

Comprobar que bandot está instalado (obviamente)

```bash
$ pip3 show bandit
Name: bandit
Version: 1.7.0
Summary: Security oriented static analyser for python code.
Home-page: https://bandit.readthedocs.io/en/latest/
Author: PyCQA
Author-email: code-quality@python.org
License: UNKNOWN
Location: /home/david/Escritorio/codigo/square_test/venv/lib/python3.6/site-packages
Requires: PyYAML, GitPython, six, stevedore
```

```bash
$ pip3 freeze | grep bandit
bandit==1.7.0
```
Meter la dependencia a bandit en `tox.ini`:

```
# ... or install anything else you might need here
deps = 
        -rrequirements.txt
        # Todas las dependencias que no se incluyan en el requirements van aqui
        # Aqui las dependencias que necesito para CI, no para dev
        black
        coverage
        bandit  <======
```


## Githooks para disparar tox pre-commit en el master

### pre-commit

https://pre-commit.com/ 

Supported hooks:

https://pre-commit.com/hooks.html


## YAML

Especificación de YAML:

https://yaml.org/spec/1.2/spec.html