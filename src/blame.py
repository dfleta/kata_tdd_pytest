from math import sqrt
from decimal import Decimal

def raiz_ecuacion_segundo_grado(a,b,c):
    if a==0:
        return None
    if b==c==0:
        return 0
    if c == 0:
        x=0
        y= -b/a
        return x,y

    if b == 0:
        if (Decimal(a).is_signed() ^ Decimal(c).is_signed()):  # XOR un comentario superlargo para ver si bandit hace lo que se supone que tiene que hacer y que propuestas de sintaxis presenta
            x = sqrt(-c/a)
            y = -sqrt(-c/a)
            return x,y
        else:
            return None

    discriminante = b**2-4*a*c

    if discriminante >= 0:
        x = (-b + sqrt(discriminante)) / (2 * a)
        y = (-b - sqrt(discriminante)) / (2 * a)
        return x, y
    else:
        return None
