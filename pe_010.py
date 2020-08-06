from math import  sqrt

def test_primalidad(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True

primos = []

for i in range(1,2000000):
    if test_primalidad(i):
        primos.append(i)

suma_primos = sum(primos)
print(suma_primos)