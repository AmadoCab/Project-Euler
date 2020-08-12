from math import sqrt

#No funciona

def fibonacci(a):
    ans = int(1/sqrt(5)*((1+sqrt(5))/2)**a-1/sqrt(5)*((1-sqrt(5))/2)**a)
    return ans

contador = 0
no_fibonacci = 0
str_fibonacci = str(no_fibonacci)

while len(str_fibonacci) < 1000:
    try:
        contador += 1
        no_fibonacci = fibonacci(contador)
        str_fibonacci = str(no_fibonacci)
    except:
        print('Error')
        break
print(contador)