'''
Ordenar utilizando el método de inserción
'''

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

def insercion(lista):
    array = copiar(lista)

    for i in range(1,len(array)):
        j = i
        aux = array[i]

        while j > 0 and array[j-1] > aux:
            array[j] = array[j-1]
            array[j-1] = aux
            j -= 1

    return array

def seleccion(lista):
    array = copiar(lista)

    for i in range(len(array)-1):
        for x in range(i+1,len(array)):
            if array[i] > array[x]:
                    aux = array[i]
                    array[i] = array[x]
                    array[x] = aux
    
    return array


#Programa principal
array = generar(int(input("Escoja la longitud de la lista a generar: ")))

print()
print("Su lista generada es:",array)
ordenada = insercion(array)
print("Su lista con el método de inserción:",ordenada)
ordenada = seleccion(array)
print("Su lista con el método de selección:",ordenada)


