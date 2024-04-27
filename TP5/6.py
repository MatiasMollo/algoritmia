'''
Leer un número e imprimir cuantos digitos tiene, el mismo puede ser negativo
'''

num = int(input("Ingrese un número: "))

contador = 0

if(num < 0):
    num *= -1

while num != 0:
    contador += 1
    num //= 10

print("El número tiene",contador,"digitos")
