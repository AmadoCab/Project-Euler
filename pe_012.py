from datetime import datetime
startTime = datetime.now()

def generador_triangular(n):
    n_triangulo = (n*(n+1))/2
    return n_triangulo

n_avo = 1
contador = 0

while contador <= 500:
    contador = 0
    divisor = 1
    n_avo = n_avo + 1
    respuesta = generador_triangular(n_avo)
    while divisor <= respuesta:
        if respuesta%divisor == 0:
            contador = contador + 1
        divisor = divisor + 1

print(f'Answer = {respuesta}')
print(datetime.now() - startTime)