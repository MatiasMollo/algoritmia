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

# Se necesita una funcion que copie la lista ya que Python devuelve la posición en memoria
def copiarLista(lista):
    array = []

    for i in range(len(lista)):
        array.append(lista[i])
    
    return array

#Devuelve una lista con los indices en orden de mayor a menor puntaje
def ordenarPorPuntaje(items):
    lista = copiarLista(items)
    indices = []
    ordenado = False
    original = items
    aux = 0

    while not ordenado:
        ordenado = True
        for i in range(len(lista) - 1):
            if(lista[i] > lista[i+1]):
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                ordenado = False
        
    for i in range(len(lista)):
        for x in range(len(lista)):
            if original[x] == lista[i]:
                indices.append(x)

    return indices

#Devuelve los indices de los participantes que superan el record
def superaRecord(record,intentos):
    lista = []

    for i in range(len(intentos)):
        if(intentos[i] <= record):
            lista.append(i)
    
    return lista

#Programa principal
jugadores = []
intentos = []
continuar = True

DIGITOS = 2

while continuar:
    #Jugador se guarda como String 
    jugador = input("Ingrese su número de documento: ")

    jugadores.append(jugador)
    intentos.append(0)
    descubierto = False

    indice = len(intentos) - 1

    print("Usted está jugando con un número de",DIGITOS,"digitos")
    aleatorio = random.randint(10**(DIGITOS-1),(10**DIGITOS)-1)

    print(aleatorio) #! Debug (no forma parte del programa)
    numero = int(input("Se ha generado un número, intente adivinarlo o ingrese -1 para finalizar: "))

    while numero != -1 and not descubierto:
        intentos[indice] += 1
        if numero == aleatorio: 
            print("¡En número aleatorio era",aleatorio,"felicidades!")
            descubierto = True
        else:
            if numero > aleatorio:
                print("El número aleatorio es menor")
            else:
                print("El número aleatorio es mayor")
            numero = int(input("Ingrese otro número: "))

    if not descubierto:
        print("Ha finalizado el juego.")
    else:
        print("Usted ha utilizado",intentos[indice],"intentos.")
    
    print()
    numero = int(input("Ingrese 1 para cargar otro jugador, presione otro número para salir: "))
    if numero != 1:
        continuar = False

if len(jugadores) > 0:
    record = int(input("Ingrese la cantidad de intentos del record: "))
    mejores = superaRecord(record,intentos)

    ordenados = ordenarPorPuntaje(intentos)

    print()
    print("Los 5 mejores jugadores son:")
    i = 0
    while i < 5 and i < len(jugadores):
        print(i + 1,"-",jugadores[ordenados[i]],"con",intentos[ordenados[i]],"intentos")
        i += 1

    if len(mejores) > 0:
        print()
        print("Los jugadores que superan el record son:")   
        for i in range(len(mejores)):
            print(i + 1,"-",jugadores[mejores[i]])
else:
    print("No se han ingresado jugadores.")




    

