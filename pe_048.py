suma_total = 0

for i in range(1000+1):
    suma_total += i**i

cadena = str(suma_total)
longitud = len(cadena)

print(cadena, end='\n')
print(cadena[longitud-10:])
print(cadena[:10])