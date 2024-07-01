'''
Resolver un problema de ordenamiento y realizar la búsqueda de un número con búsqueda binaria
'''
import random

def generar(longitud):
    lista = []
    for i in range(longitud):
        lista.append(random.randint(0,100))
    return lista

def copiar(lista):
    array = []
    for i in range(len(lista)):
        array.append(lista[i])

    return array

def ordenar(lista):
    array = copiar(lista)
    ordenado = False
    aux = 0

    while not ordenado:
        ordenado = True

        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                aux = array[i]
                array[i] = array[i+1]
                array[i+1] = aux
                ordenado = False

    return array

def buscar(lista,numero):
    i = 0
    d = len(array)-1
    posicion = -1

    while i <= d and posicion == -1:
        c = (i+d)//2 # Se obtiene el centro del array

        if lista[c] == numero:
            posicion = c
        elif lista[c] < numero:
            i = c + 1
        else:
            d = c - 1
    
    return posicion




#Programa principal
array = generar(int(input("Escoja la longitud de la lista a generar: ")))

print()
print("Su lista generada es:",array)
ordenada = ordenar(array)
print("Su lista ordenada es:",ordenada)

numero = int(input("Ingrese un número a buscar: "))

posicion = buscar(ordenada,numero)

if posicion == -1: 
    print("No se ha encontrado ese numero")
else:
    print("Posicion",posicion)