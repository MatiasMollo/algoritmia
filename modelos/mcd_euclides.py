'''
Encontrar el MCD de dos números dados
'''

n1 = int(input("Ingrese el número 1: "))
n2 = int(input("Ingrese el número 2: "))

mcd = 0
actual = 1

if n1 > n2:
    menor = n2
else:
    menor = n1

if n1 == 0:
    mcd = n2
elif n2 == 0:
    mcd = n1
else: 
    while actual <= menor:
        if n1%actual == 0 and n2%actual == 0:
            mcd = actual
        actual += 1

print("MCD:",mcd)