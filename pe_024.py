import itertools as it

numeros_permutar = '0123456789'
longitud = len(numeros_permutar)
contador = 0
resultado = ''

for i in it.permutations(numeros_permutar, longitud):
    contador += 1
    if contador == 1000000:
        for j in i:
            resultado += str(j)
        print(resultado)
        break
    else:
        pass