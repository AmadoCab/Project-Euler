bigest = 0

def palindromo(numero_str):
    if numero_str == numero_str[::-1]:
        return True
    return False

for i in range(100, 1000):
    for j in range(100, 1000):
        numero_int = i*j
        if numero_int > bigest and palindromo(str(numero_int)):
            bigest = i*j

print(bigest)