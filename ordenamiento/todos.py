'''
Armar funciones con todos los metodos de ordenamientos explicados en clase

Inserción, selección y burbuja.
Luego, realizar la búsqueda de un número con el método de búsqueda binaria
'''

import random

def copiar(lista):
    array = []
    for i in range(len(lista)):
        array.append(lista[i])
    return array

def burbuja(lista):
    a = copiar(lista)
    ordenado = False

    while not ordenado:
        ordenado = True
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                aux = a[i]
                a[i] = a[i+1]
                a[i+1] = aux
                ordenado = False
    return a

def insercion(lista):
    a = copiar(lista)

    for i in range(1,len(a)):
        aux = a[i]
        x = i

        while x > 0 and a[x-1] > aux:
            a[x] = a[x-1]
            a[x-1] = aux
            x -= 1
    return a

def seleccion(lista):
    a = copiar(lista)

    for i in range(len(a)-1):
        for x in range(i,len(a)):
            if a[i] > a[x]:
                aux = a[i]
                a[i] = a[x]
                a[x] = aux
    return a 

def generar(cantidad):
    a = []
    for i in range(cantidad):
        a.append(random.randint(0,100))
    return a

def binario(lista,elemento):
    i = 0
    d = len(lista)-1
    posicion = -1

    while i <= d and posicion == -1:
        c = (i + d) // 2

        if(lista[c] == elemento):
            posicion = c
        elif lista[c] < elemento:
            i = c+1
        else:
            d = c-1

    return posicion

array = generar(int(input("Ingrese la cantidad de items a generar: ")))
print("Su array es:",array)

bur = burbuja(array)
print("Ordenado con burbuja:",bur)
print("Ordenado con inserción:",insercion(array))
print("Ordenado con selección:",seleccion(array))

pos = binario(bur,int(input("Ingrese el número a buscar: ")))

if pos == -1:
    print("No se ha encontrado ese número en la lista")
else:
    print("El número se encuentra en la posición",pos)
