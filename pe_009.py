from math import pow

for a in range(0,1000):
    for b in range(0,1000):
        for c in range(0,1000):
            if a+b+c==1000:
                if pow(a,2)+pow(b,2)==pow(c,2):
                    print(f'Los numeros son: {a}, {b} y {c}')
                    print(f'y su producto es: {a*b*c}')