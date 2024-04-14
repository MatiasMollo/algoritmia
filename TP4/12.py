'''
Hacer un programa que calcule los numeros fibonacci hasta el input ingresado
'''

limite = int(input("Ingrese el número limite de la sucesion de Fibonacci: "))

a = 0
b = 1
suma = 0
cont = 0

while cont <= limite:
    print(suma)
    a = b
    b = suma
    suma = a + b
    cont += 1