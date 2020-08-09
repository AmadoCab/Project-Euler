# Función factorial
def factorial(numero):
    """La función recibe un numero y regresa el factorial de este"""
    resultado = 1
    for i in range(1, numero+1):
        resultado *= i
    return resultado

# Lista por comprensión que almacena todos los dígitos del factorial de 100
suma_digitos = [int(j) for j in str(factorial(100))]
print(sum(suma_digitos))