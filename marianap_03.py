from math import sqrt

respuesta=1

def test_primalidad(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True


for n in range(1,int(sqrt(600851475144))):
    if (600851475143%n==0 and test_primalidad(n)):
        if n>respuesta:
            respuesta=n
print(respuesta)