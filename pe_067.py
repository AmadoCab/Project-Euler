def reducción_piramidal(matriz):
    tabla = matriz
    longitud = len(tabla[-1])
    if longitud == 1:
        print(matriz[0][0])
    else:
        for i in range(longitud-1):
            if tabla[-1][i] > tabla[-1][i+1]:
                tabla[-2][i] += tabla[-1][i]
            elif tabla[-1][i] < tabla[-1][i+1]:
                tabla[-2][i] += tabla[-1][i+1]
            elif tabla[-1][i] == tabla[-1][i+1]:
                print(True)
        tabla.remove(tabla[-1])
        reducción_piramidal(tabla)

triangulo = []

with open('triangulo.txt', 'r') as f:
    for i in range(100):
        variable = f.readline().strip().split()
        variable = [int(n) for n in variable]
        triangulo.append(variable)

#print(triangulo)

reducción_piramidal(triangulo)
