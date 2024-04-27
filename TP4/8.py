'''
Ingresar números hasta que la suma de los pares supere el número 100.
Mostrar cuantos números se ingresaron en total
'''

suma = 0
contador = 1
numero = int(input("Ingrese un número (0 para finalizar): "))

while suma < 100 and numero != 0:
    numero = int(input("Ingrese un número (0 para finalizar): "))
    contador += 1

    if numero % 2 == 0:
        suma += numero

print("La suma de numeros pares es", suma,", se han ingresado un total de",contador,"numeros")