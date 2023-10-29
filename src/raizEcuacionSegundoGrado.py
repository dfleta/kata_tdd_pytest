from math import sqrt
from decimal import Decimal


def raiz_ecuacion_segundo_grado(a, b, c):

    if a == 0:
        return None

    if b == c == 0:
        return 0

    if c == 0:
        x = 0
        y = -b / a
        return x, y

    if b == 0:
        if Decimal(a).is_signed() ^ Decimal(c).is_signed():  # XOR
            x = sqrt(-c / a)
            y = -sqrt(-c / a)
            return x, y
        else:
            return None

    discriminante = b ** 2 - 4 * a * c

    if discriminante >= 0:
        x = (-b + sqrt(discriminante)) / (2 * a)
        y = (-b - sqrt(discriminante)) / (2 * a)
        return x, y
    else:
        return None


if __name__ == '__main__':

    # test_b_nulo_solucion_real():
    assert raiz_ecuacion_segundo_grado(1, 0, -1) == (1, -1)

    # test_discriminante_cero()
    assert raiz_ecuacion_segundo_grado(1, 2, 1) == (-1, -1)

    # test_discriminante_positivo()
    assert raiz_ecuacion_segundo_grado(1, -1, -2) == (2, -1)

    # def test_discriminante_negativo()
    assert raiz_ecuacion_segundo_grado(1, 1, 1) is None

    # test_soluciones_fraccion()
    assert raiz_ecuacion_segundo_grado(6, -7, 2) == (2 / 3, 1 / 2)
