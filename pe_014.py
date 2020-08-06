def collatz_len_cadena(numero):
    resultado = numero
    contador = 1
    while resultado != 1:
        if resultado == 0:
            return contador
        elif resultado%2 == 0:
            resultado = resultado/2
            contador += 1
        else:
            resultado = 3*resultado+1
            contador += 1
    return contador

longitud_maxima = 0

for i in range(1000000):
    if collatz_len_cadena(i)>longitud_maxima:
        longitud_maxima = collatz_len_cadena(i)
        print(f'El número es {i} y la longitud de su cadena es de {longitud_maxima}')
    else:
        pass