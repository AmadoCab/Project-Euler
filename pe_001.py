suma = 0
cota = int(input("ingrese hasta que numero quiere sumar los multiplos de 3 o 5: "))

for i in range(0,cota):
    if i%3==0:
        suma = suma + i
    elif i%5==0:
        suma = suma + i
    else:
        pass
print(suma)
