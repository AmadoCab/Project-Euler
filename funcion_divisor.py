def divisores(n):
    lista_divisores = []
    lista_divisores.append(f'{n}:')
    divisor = 1
    while divisor <= n :
        if n%divisor == 0:
            lista_divisores.append(divisor)
        divisor += 1
    return lista_divisores

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

print(n_avo)
print(respuesta)
print('\n\n')
x = int(input('ingrese un numero\n'))
print(generador_triangular(x))
x = int(input('ingrese un numero\n'))
print(generador_triangular(x))
x = int(input('ingrese un numero\n'))
print(generador_triangular(x))