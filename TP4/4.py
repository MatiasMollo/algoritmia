'''
Desarrollar un programa que imprima la suma de los números impares
comprendidos entre el 42 y el 176
'''

suma = 0
numero = 42

while numero < 176:
    if (numero%2 != 0):
        suma += numero
        numero += 2
    else: numero += 1

print("La suma es: ", suma)