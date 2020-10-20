# importar el modulo de otro directorio
from src.raizEcuacionSegundoGrado import raiz_ecuacion_segundo_grado
import pytest


@pytest.mark.c_nulo
def test_c_nulo():
    assert raiz_ecuacion_segundo_grado(1, 1, 0) == (0, -1)

@pytest.mark.c_nulo
def test_c_nulo():
    assert raiz_ecuacion_segundo_grado(2, 4, 0) == (0, -2)


