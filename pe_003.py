from math import sqrt

def test_primalidad(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True

print("inicia programa\n")

numero = 600851475143
factor = numero

for i in range(2,int(sqrt(numero))+1):
    if test_primalidad(i) and numero%i==0:
        factor = factor/i
        if factor == 1:
            print("ya vas\n")
            print(i)
            break
        else:
            pass
    else:
        pass
