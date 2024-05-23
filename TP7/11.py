'''
cargar dos listas de números A y B con N números al azar entre 1 y 100
N se ingresa por teclado

Luego imprimir 3 listas C D y E que contengan
- La concatenación de los valores pares de A con los impares de B
- La concatenación de los valores impares de A con el deverso de los pares de B
- La intercalación de los elementos de A y B
'''

import random

def completar(cantidad):
    array = []
    for i in range(cantidad):
        array.append(int(random.random() * 100))

    return array

def filtrar(array, par):
    ret = []
    par = False

    for i in range(len(array)):
        if par and array[i]%2 == 0:
            ret.append(array[i])
        elif not par and array[i]%2 == 0:
            ret.append(array[i])

    return ret

def revertir(array):
    ret = []

    for i in range(0,len(array),-1):
        ret.append(array[i])

    return ret

def concatenar(array1,array2):
    for i in range(len(array2)):
        array1.append(array2[i])

    return array1

def intercalar(array1, array2):
    i = 0
    x = 0


#! Filtrar valores negativos
a = completar(int(input("Ingrese la cantidad de valores que tendrá A: ")))
b = completar(int(input("Ingrese la cantidad de valores que tendrá B: ")))



