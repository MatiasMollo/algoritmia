'''
Ingresar un número, verificar si es positivo
Mostrar los números impares hasta el número ingresado
Informar la suma de los números impares

Si se ingresa 5, se debe mostrar 1 3 y 5, y su suma es 9
'''

numero = int(input("Ingrese un número positivo: "))
contador = 0
suma = 1

while contador == 0:
    if numero > 0:
        contador = 1
        while contador+1 < numero:
            print("impares:",contador)
            contador += 2
            suma += contador
        
        if numero % 2 == 1:
            print("Impares:",numero)
    else:
        numero = int(input("El número ingresado no es positivo, intente nuevamente: "))

print("suma: ",suma)
