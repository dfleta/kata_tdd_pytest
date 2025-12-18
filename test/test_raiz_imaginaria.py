# importar el modulo de otro directorio
from src.raizEcuacionSegundoGrado import raiz_ecuacion_segundo_grado
import pytest


@pytest.mark.b_c_nulo
def test_raiz_nula_unica():
    assert raiz_ecuacion_segundo_grado(1, 0, 0) == 0


@pytest.mark.discriminante
@pytest.mark.parametrize("a,b,c", [
    (1, 1, 1),    # discriminante = 1 - 4 = -3
    (2, 3, 4),    # discriminante = 9 - 32 = -23
    (5, 1, 2),    # discriminante = 1 - 40 = -39
])
def test_discriminante_negativo(a, b, c):
    """Casos donde el discriminante es negativo => raíces imaginarias -> None."""
    assert raiz_ecuacion_segundo_grado(a, b, c) is None


@pytest.mark.b_nulo
@pytest.mark.parametrize("a,c", [
    (1, 1),   # a y c con el mismo signo -> raíces imaginarias
    (-1, -1), # ambos negativos -> raíces imaginarias
])
def test_b_nulo_raices_imaginarias(a, c):
    """Cuando b==0 y a y c tienen el mismo signo las raíces son imaginarias."""
    assert raiz_ecuacion_segundo_grado(a, 0, c) is None

