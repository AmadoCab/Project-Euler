from math import sqrt
import csv

# Funciones
def punctuation(nombre):
    """Esta función recibe una cadena, sustituye cada letra por su respectivo
    valor en decimal con la función 'traductor' y los suma"""
    lista_caracteres = [int(traductor(n)) for n in nombre]
    resultado = sum(lista_caracteres)
    return resultado

def traductor(caracter):
    """Sustituye cada caracter de una cadena por su respectivo en decimal"""
    tabla = {
        'A':'1', 'B':'2', 'C':'3', 'D':'4', 'E':'5', 'F':'6', 'G':'7', 'H':'8', 
        'I':'9', 'J':'10', 'K':'11', 'L':'12', 'M':'13', 'N':'14', 'O':'15', 
        'P':'16', 'Q':'17', 'R':'18', 'S':'19', 'T':'20', 'U':'21', 'V':'22', 
        'W':'23', 'X':'24', 'Y':'25', 'Z':'26', ' ':' '
    }
    resultado = caracter
    for i in resultado:
        resultado = resultado.replace(i, tabla.get(i, '?'))
    return resultado

def es_triangular(numero):
    enesimo = (-1+sqrt(1+8*numero))/(2)
    if enesimo - int(enesimo) == 0:
        return True
    else:
        return False

contador = 0

# Abrir el archivo de los nombres y leerlos
with open('palabras.txt', 'r') as f:
    total = 0
    csv_reader = csv.reader(f)
    for line in csv_reader:
        longitud = len(line)
        for i in range(longitud):
            valor = punctuation(line[i])
            if es_triangular(valor):
                contador += 1
        print(contador)
