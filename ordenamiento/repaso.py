'''
Programar los distintos métodos de ordenamiento y búsqueda
'''

def copiar (lista):
    array = []

    for i in range(len(lista)):
        array.append(lista[i])

    return array

def insercion(lista):
    lista = copiar(lista)

    for x in range(1,len(lista)):
        aux = lista[x]
        i = x

        while i > 0 and lista[i-1] > aux:
            lista[i] = lista[i-1]
            lista[i-1] = aux
            i -= 1

    return lista

def seleccion(lista):
    lista = copiar(lista)

    for i in range(len(lista)-1):
        for x in range(i,len(lista)):
            if lista[i] > lista[x]:
                aux = lista[i]
                lista[i] = lista[x]
                lista[x] = aux

    return lista


def burbuja (lista):
    lista = copiar(lista)
    ordenado = False

    while not ordenado:
        ordenado = True
        for i in range(len(lista)-1):
            if(lista[i] > lista[i+1]):
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                ordenado = False

    return lista

#Metodos de ordenamiento

def binario(lista,elemento):
    i = 0
    d = len(lista)-1
    posicion = -1
    posiciones = []

    while i <= d and posicion == -1:
        c = (i + d) // 2

        if lista[c] == elemento:
            posicion = c
            posiciones.append(posicion)
            
            #Modificación para encontrar todos las posiciones del elemento
            x = c - 1
            while x > 0 and lista[x] == elemento:
                posiciones.append(x)
                x -= 1

            x = c + 1
            while x < len(lista) and lista[x] == elemento :
                posiciones.append(x)
                x += 1

        elif lista[c] > elemento:
            d = c - 1
        else:
            i = c + 1

    return posiciones

#Principal
lista = [5,3,6,34,8,11,34,734,2,54,12,576,34,34]

print("Lista:",lista)
print("Inserción:",insercion(lista))
print("Selección:",seleccion(lista))
print("Burbuja  :",burbuja(lista))
print()
print('Posición:',binario(burbuja(lista),34))
