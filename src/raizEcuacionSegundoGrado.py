
from math import sqrt

# sonar lint marca como code smell la notacion camel case
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
        x = sqrt(-c/a)
        y = -sqrt(-c/a)
        return x, y
    

    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        x = (-b + sqrt(discriminante)) / (2 * a)
        y = (-b - sqrt(discriminante)) / (2 * a)
        return x, y
    else:
        return None
  

if __name__ == "_main__":

    x, y = raiz_ecuacion_segundo_grado(1, 1, 0)
    assert x == 0
    assert y == -1

    x, y = raiz_ecuacion_segundo_grado(2, 4, 0)
    assert x == 0
    assert y == -2

    x, y = raiz_ecuacion_segundo_grado(1, 0, -1)
    assert x == 1
    assert y == -1
