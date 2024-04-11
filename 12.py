'''
Hacer un programa que calcule los numeros fibonacci hasta el input ingresado
'''

limite = int(input("Ingrese el número limite de la sucesion de Fibonacci: "))

a = 0
b = 1
cont = 0

while cont <= limite:
    print(a)
    a = a+b
    b = a
    cont += 1