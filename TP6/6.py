'''
Función comparar(a,b). Recibe dos números enteros y devuelve 1 si a > b. 0 si son iguales
y -1 si b > a. Reutilizando la función signo del programa anterior
'''

#Función de 5.py
def signo (numero):
    signo = 0
    if numero > 0:
        signo = 1
    elif numero < 0:
        signo = -1
    return signo

def comparar (a,b):
    return signo(b - a)

a = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número: "))

print('Devolución: ',comparar(a,b))