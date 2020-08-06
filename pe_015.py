tamaño_matriz = 20

matriz = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

# 0 movimiento a la derecha
# 1 movimiento hacia abajo

for i in range(tamaño_matriz+1):
    for j in range(tamaño_matriz+1):
        if i == tamaño_matriz and j == tamaño_matriz:
            matriz[i][j] = True
        elif i == tamaño_matriz:
            matriz[i][j] = 0
        elif j == tamaño_matriz:
            matriz[i][j] = 1
        else:
            matriz[i][j] = (0, 1)

print(matriz)

def caminos(arreglo, iniciox=0, inicioy=0):
    suma = 0
    if type(tuple([1,2,3])) == type(arreglo[iniciox][inicioy]):
        for x in arreglo[iniciox][inicioy]:
            if x == 0:
                suma = suma + caminos(arreglo, iniciox, inicioy+1)
            elif x == 1:
                suma = suma + caminos(arreglo, iniciox+1, inicioy)
    elif type(1) == type(arreglo[iniciox][inicioy]):
        if arreglo[iniciox][inicioy] == 0:
            suma = suma + caminos(arreglo, iniciox, inicioy+1)
        elif arreglo[iniciox][inicioy] == 1:
            suma = suma + caminos(arreglo, iniciox+1, inicioy)
    else:
        suma = suma+1
    return suma


total = caminos(matriz)
print(total)