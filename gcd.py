def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a < b:
        return gcd(a,b%a)
    elif a > b:
        return gcd(b, a%b)

print(gcd(2020,3000276))
print(gcd(3000276,2020))
