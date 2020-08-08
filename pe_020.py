def factorial(numero):
    resultado = 1
    for i in range(1, numero+1):
        resultado *= i
    return resultado

suma_digitos = [int(j) for j in str(factorial(100))]
print(sum(suma_digitos))