'''
Rellenar una lista con números enteros entre 0 y 100 obtenidos al azar
e imprimir el valor mínimo y el lugar que ocupa.

Tener en cuenta que el mínimo puede estar repetido (en ese caso deberán mostrarse todas las posiciones)

La carga de datos termina cuando se carga 0 como número al azar, el cual no deberá cargarse en la lista
'''

import random

def rellenar ():
    lista = []
    numero = random.randint(0,100)

    while numero != 0:
        lista.append(numero)
        numero = random.randint(0,100)

    return lista


def buscarMinimo(lista):
    i = 0
    while i < len(lista):
        if i == 0:
            minimo = lista[i]
        elif lista[i] < minimo:
            minimo = lista[i]
        i += 1

    return minimo

def buscarPosiciones(lista,numero):
    posicion = []
    for i in range(len(lista)):
        if lista[i] == numero:
            posicion.append(i)
    return posicion


# Programa principal
lista = rellenar()
minimo = buscarMinimo(lista)

print("Lista:",lista)
posiciones = buscarPosiciones(lista,minimo)
print("El número mínimo es",minimo,"y se encuentra en las posiciones ",posiciones)