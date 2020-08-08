# Esta función es la encargada de hacer las comparaciones en la matriz
def reducción_piramidal(matriz):
    """La función recibe como parametro una matriz triangular inferior"""
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
                tabla[-2][i] += tabla[-1][i+1]
        tabla.remove(tabla[-1])
        reducción_piramidal(tabla)

# Aquí almacenaremos la matriz triangular que obtendremos del documento \
# triangulo.txt
triangulo = []

# Aquí leemos el documento y lo convertimos en listas numéricas con las que \
# podamos trabajar
with open('triangulo.txt', 'r') as f:
    for i in range(100):
        variable = f.readline().strip().split()
        variable = [int(n) for n in variable]
        triangulo.append(variable)

reducción_piramidal(triangulo)
