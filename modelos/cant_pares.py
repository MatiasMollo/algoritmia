# Ingresar cant de numeros, informar si la cantidad es par o no. No usar contadores, finalizar carga con -1

par = True
i = 0
num = int(input("Ingrese un número: "))

while num != -1:
    i = 1
    par = not par
    num = int(input("Ingrese otro número, -1 para finalizar: "))

if i > 0:
    if par:
        print("La cantidad de números es par")
    else:
        print("La cantidad de números es impar")
else:
    print("No se han ingresado números")