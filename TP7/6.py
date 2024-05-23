'''
Escribir función para devolver una lista con todas las posiciones
que ocupa un valor pasado como parametro, utilizando búsqueda secuencial en una lista
desordenada.

Si el elemento no se encuentra, la función debe devolver una lista vacía
'''

import random

# Genera una lista aleatoria con números del 0 al 100
def generarLista(longitud):
    if longitud < 0:
        longitud = 1

    lista = []

    for i in range(longitud):
        lista.append(random.randint(0,100))

    return lista


def buscar (lista,numero):
    pos = []

    for i in range(len(lista)):
        if lista[i] == numero:
            pos.append(i)

    return pos

#programa principal
lista = generarLista(int(input("Ingrese la longitud de la lista a generar: ")))
print("La lista generada es la siguiente: ", lista)

numero = int(input("Ingrese el número a buscar en la lista: "))
print("Las posiciones en las que aparece el número son:",buscar(lista,numero))
