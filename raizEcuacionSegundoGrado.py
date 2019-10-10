
from math import sqrt

def raizEcuacionSegundoGrado(a, b, c):
    
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
  

if __name__ == "_main__":

    x, y = raizEcuacionSegundoGrado(1, 1, 0)
    assert x == 0
    assert y == -1

    x, y = raizEcuacionSegundoGrado(2, 4, 0)
    assert x == 0
    assert y == -2

    x, y = raizEcuacionSegundoGrado(1, 0, -1)
    assert x == 1
    assert y == -1


