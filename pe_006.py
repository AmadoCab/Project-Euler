from math import pow

superior = 100

numeros = list(range(0, superior+1))
cuadrado_numeros = [int(pow(n, 2)) for n in numeros]

suma_numeros_cuadrado = int(pow(sum(numeros),2))
suma_cuadrado_numeros = int(sum(cuadrado_numeros))
resultado = suma_numeros_cuadrado-suma_cuadrado_numeros

print(f'{suma_numeros_cuadrado}-{suma_cuadrado_numeros}={resultado}')