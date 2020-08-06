from math import sqrt

def test_primalidad(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True

contador = 0
respuesta = 0

for i in range(110000):
    if test_primalidad(i) and contador<=10001:
        contador = contador + 1
        respuesta = i
    elif contador>10001:
        break
    else:
        pass

print(respuesta)