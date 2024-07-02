'''
Obtener N° random de 4 cifras, el usuario debe adivinarlo informando si la entrada
es mayor o menor al mismo.
Para cortar el juego se ingresa -1

Al terminar el juego informar:
- Cantidad de intentos realizada, haciendo que ingrese su N° de documento si mejoró la mejor
marca de intentos obtenida hasta el momento
- Mostrar la lista ordenada de los 5 mejores puntajes (indicando a quien pertenecen)

Al finalizar el juego preguntar si se desea seguir jugando y reiniciarlo
'''

import random

def copiar(lista):
    array = []
    for i in range(len(lista)):
        array.append(lista[i])

    return array

def ordenar(lista):
    lista = copiar(lista) #Obtiene una nueva lista y no ordena la anterior por la forma en la que python guarda los punteros de memoria
    ordenado = False

    while not ordenado:
        ordenado = True
        for i in range(len(lista)-1):
            if (lista[i] > lista[i+1]):
                ordenado = False
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
    return lista

def indices(original,lista):
    array = []
    for i in range(len(original)):
        for x in range(len(lista)):
            if original[i] == lista[x]:
                array.append(x)
    return array

#Programa principal
CIFRAS = 2
continuar = True

jugadores = []
puntos = []

while continuar:
    numero = random.randint(10**(CIFRAS-1),(10**CIFRAS)-1)
    print("Usted está jugando con un número de",CIFRAS,"cifras")
    intentos = 0

    print("Numero:",numero) #! Debug (no forma parte del programa)

    ingreso = int(input("Ingrese su número (-1 para finalizar): "))

    while ingreso != -1 and continuar:
        intentos += 1
        if numero == ingreso:
            print("Numero acertado, usted ha utilizado",intentos,"intentos")

            menor = 0
            for i in range(len(puntos)):
                if i == 0 or puntos[i] < menor:
                    menor = puntos[i]

            if intentos < menor or len(puntos) == 0:
                jugador = input("Supero record, ingrese su Nro de documento: ")
                while jugador == '':
                    jugador = input("Dato incorrecto, intente nuevamente: ")
                
                jugadores.append(jugador)
                puntos.append(intentos)

            seguir = int(input("¿Desea seguir? 1 para SI, otro número para salir: "))
            ingreso = -1 #Forzamos la salida del bucle mas cercano para que actualice el número a adivinar
            if seguir != 1:
                continuar = False

        else:
            if numero < ingreso:
                print("El número es menor")
            else:
                print("El número es mayor")

            ingreso = int(input("Ingrese su número: "))
            
  
if len(jugadores) > 0:
    intentosOrdenados = ordenar(puntos)
    ordenados = indices(puntos,intentosOrdenados) #Array de indices en orden

    print()
    print("Lista de puntos")
    recorrido = len(ordenados)
    if recorrido > 6:
        recorrido = 6
    for i in range(recorrido):
        indice = ordenados[i]
        print(i+1,jugadores[indice],'con',puntos[indice],'intentos')
else:
    print("No se han registrado juegos completados")


