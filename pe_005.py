from math import sqrt, pow

def prod(lista):
    producto = 1
    for i in lista:
        producto = producto * i
    return producto

def test_primalidad(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True

numero_superior = 200

numeros = list(range(1,numero_superior+1))
primos = []
exponentes = []
respuesta = 1

for i in numeros:
    if test_primalidad(i):
        primos.append(i)
    else:
        pass

for i in primos:
    for j in range(numero_superior):
        if pow(i,j)<numero_superior:
            pass
        else:
            exponentes.append(j-1)
            break

for i in range(len(primos)):
    respuesta = respuesta * pow(primos[i],exponentes[i])

respuesta = int(respuesta)

print(primos)
print(exponentes)
print(f'\n{respuesta}')