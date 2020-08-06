from math import sqrt

suma = 0

def fibonacci(a):
    ans = int(1/sqrt(5)*((1+sqrt(5))/2)**a-1/sqrt(5)*((1-sqrt(5))/2)**a)
    return ans

i=0

while fibonacci(i)<4000000:
    if fibonacci(i)%2==0:
        suma = suma + fibonacci(i)
    i += 1

print(suma)
