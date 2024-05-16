'''
Dada una lista ordenada "A" y un nuevo número "N", desarrollar un programa
que inserte N en A en el orden correspondiente. El mismo debe detectar si el orden
es ascendente o descendente antes de realizar la inserción.

No se permite agregar el elemento al final y reordenar la lista
'''

#Devuelve 0 si no está ordenado, 1 si es ascendente y -1 si es descendente
def verifyOrder(array):
    ret = 0
    ascendente = True
    descendente = True
    i = 0

    while i < len(array) - 1 and ascendente:
        ret = 1
        if array[i] > array[i + 1]:
            ascendente = False
        i += 1

    i = 0

    while i < len(array) - 1 and descendente:
        if array[i] < array[i + 1]:
            descendente = False
        i += 1

    if ascendente and not descendente:
        ret = 1
    elif not ascendente and descendente:
        ret = -1
    else:
        ret = 0

    return ret

def insertNum(array,num,order):
    newArray = []
    inserted = False

    for i in range(len(array)):
        if not inserted:    
            if num < array[i] and order == 1:
                newArray.append(num)
                inserted = True
            elif num > array[i] and order == -1:
                newArray.append(num)
                inserted = True
                
        newArray.append(array[i])

    return newArray

a = []
numero = input("Ingrese un número ('#' para finalizar): ")

while numero != '#':
    a.append(int(numero))
    numero = input("Ingrese un número ('#' para finalizar): ")

numero = int(input("Ingrese el nuevo número para meter en el array: "))

orden = verifyOrder(a)

if orden != 0:
    print("La nueva lista es:",insertNum(a,numero,orden))
else:
    print("La lista ingresada no está ordenada")




