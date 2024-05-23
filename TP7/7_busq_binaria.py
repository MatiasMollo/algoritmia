'''
Realizar una función que devuelva una array con las posiciones de un elemento en una lista
Implementar búsqueda binaria sobre una lista ordenada
'''

def ordenar (lista):
    aux = 0

    #Filtrado de listas vacías
    if len(lista) == 0:
        lista.append(0)

    for i in range(len(lista ) - 1):
        for x in range(i + 1,len(lista)):
            if lista[x] < lista[i]:
                aux = lista[x]
                lista[x] = lista[i]
                lista[i] = aux

    return lista

def busqueda (lista,numero):
    lista = ordenar(lista)
    print("Lista ordenada:",lista)
    posiciones = []

    i = 0
    d = len(lista) - 1
    posicion = -1
    
    while i <= d and posicion == -1:
        #Obtenemos la posición central (si es impar se redondea hacia abajo)
        c = (i + d)// 2

        if lista[c] == numero:
            # Se agrega el indice a la lista y se cambia la posición para que rompa el bucle
            posiciones.append(c)

            # La posicion pasa a ser una antes del centro para encontrar los elementos que están a la izquierda
            posicion = c - 1

            # Si la el numero buscado se encuentra a la izquierda se sigue agregando y se le resta 1 a posicion
            while lista[posicion] == numero and posicion > 0:
                posiciones.append(posicion)
                posicion -=1
            
            # La posición pasa a ser una despues del centro para buscar los elementos de la derecha
            posicion = c + 1

            # Se hace los mismo que cuando se busca por izquierda
            while lista[posicion] == numero and posicion < len(lista):
                posiciones.append(posicion)
                posicion += 1

            # Ordenamos las tabla de posiciones
            posiciones = ordenar(posiciones)

        # Si el número del centro no es el que buscamos, y el N actual es menor al numero de la posición, cambiamos el valor de izquierda
        elif lista[c] < numero:
            i = c + 1
        else:
            # De lo contrario, cambiamos el valor de la derecha
            d = c - 1

    return posiciones


print("Posiciones:",busqueda([20,20,2,4,5,1,20,4,2,32,10,20,430,320,43,524,54,74,546,20],20))