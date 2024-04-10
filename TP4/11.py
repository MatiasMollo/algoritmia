'''
Leer un numero e indicar si es primo o no
'''

numero = int(input("Ingrese el numero: "))
index = 2
primo = True

while numero > index:
    if numero%index == 0:
        print(index)
        primo = False
        break
    index += 1

if numero > 0:
    if primo: print("El numero es primo")
    else: print("El numero no es primo")
else: print("No existen numeros primos negativos")