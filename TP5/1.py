'''
Leer edades, finalizar programa cuando se ingresa '-1'. Imprimir cuantos son menores y descartar edades >100 y <0
'''

edad = mayores = menores = 0

while edad != -1:
    edad = int(input("Ingrese la edad: "))

    if edad >= 0 and edad <= 100:
        if edad >= 18: mayores += 1
        else: menores += 1

print('Mayores: ',mayores,'\nMenores: ',menores)


