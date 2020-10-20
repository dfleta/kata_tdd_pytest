# importar el modulo de otro directorio
from src.raizEcuacionSegundoGrado import raiz_ecuacion_segundo_grado
import pytest

@pytest.mark.b_c_nulo
def test_raiz_nula_unica():
    assert raiz_ecuacion_segundo_grado(1, 0, 0) == 0
