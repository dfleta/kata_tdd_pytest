# importar el modulo de otro directorio
from src.raizEcuacionSegundoGrado import raiz_ecuacion_segundo_grado
import pytest


@pytest.mark.b_nulo
def test_b_nulo_solucion_real():
    assert raiz_ecuacion_segundo_grado(1, 0, -1) == (1, -1)
    assert raiz_ecuacion_segundo_grado(-1, 0, 1) == (1, -1)


@pytest.mark.b_nulo
def test_b_nulo_solucion_imaginaria():
    assert raiz_ecuacion_segundo_grado(1, 0, 1) == None
    assert raiz_ecuacion_segundo_grado(-1, 0, -1) == None
