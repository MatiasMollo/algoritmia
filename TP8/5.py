'''
Modificar el programa 4 para que las pistas brindadas no sean de tipo 
"es mayor" o "es menor" sino que sean "M digitos correctos" y "N digitos aproximados"

Se considera que el dígito es correcto cuando su valor como posición coincide con el del
número aleatorio. Mientras que un dígito es aproximado cuando coincide el valor pero
no su posición
'''

import random

DIGITOS = 2

#Indica cuantos números con posición correcta hay
def digitosCorrectos(original,numero):
    contador = 0

    while original != 0 and numero != 0:
        if numero%10 == original%10:
            contador += 1
        
        numero //= 10
        original //= 10

    return contador

#Devuelve la cantidad de dígitos que se encuentran en el número original (con posición distinta)
def digitosAproximados(original,numero):
    contador = 0
    numeros = []
    originales = []

    #Convierte un número en una lista en donde cada indice contiene un dígito
    while numero != 0:
        numeros.append(numero%10)
        numero //= 10

    while original != 0:
        originales.append(original%10)
        original //= 10

    #Se recorren ambas listas y se comparan sus valores
    for i in range(len(originales)):
        for x in range(len(numeros)):
            if numeros[x] == originales[i] and x != i:
                contador += 1

    return contador


def superoRacha(intentos,mejores):
    supero = False

    if len(mejores) <= 0:
        supero = True
    elif mejores[len(mejores)-1][1] >= intentos: #Verifica que los intentos del último jugador sean mayores a los intentos del ultimo jugador
        supero = True
    
    return supero

def ordenarMejores(mejores):
    ordenado = False
    aux = 0

    while not ordenado:
        ordenado = True

        for i in range(len(mejores)-1):
            if mejores[i][1] >= mejores[i+1][1]:
                aux = mejores[i]
                mejores[i] = mejores[i+1]
                mejores[i+1] = aux
                ordenado = False

    return mejores



continuar = True
mejores = [] #Matriz que guarda los jugadores con los mejores intentos

while continuar:
    print()
    intentos = 0
    descubierto = False

    aleatorio = random.randint(10**(DIGITOS-1),(10**DIGITOS)-1)

    # print("N° aleatorio: ",aleatorio) #! DEBUG

    numero = int(input("Ingrese un número o presione -1 para salir: "))

    while numero != -1 and not descubierto:

        intentos += 1

        if numero == aleatorio:
            print("¡Felicidades! el número era",aleatorio,"- usted ha utilizado",intentos,"intentos")
            descubierto = True
            print()

            if superoRacha(intentos,mejores):
                jugador = input("Superó la racha anterior. Ingrese su Nro de documento: ")
                mejores.append([jugador,intentos])
        else: 
            correctos = digitosCorrectos(aleatorio,numero)
            aproximados = digitosAproximados(aleatorio,numero)
            print(correctos,"dígitos correctos")
            print(aproximados,"dígitos aproximados")

            numero = int(input("Ingrese otro número: "))

    if numero == -1:
        print()
        print("Los mejores puntajes son: ")
        ordenados = ordenarMejores(mejores)
        i = 0
        while i < 5 and i < len(ordenados):
            print(i+1,"-",ordenados[i][0],"con",ordenados[i][1],"intentos")
            i += 1
        
        mejores = []

        otroJugador = input("¿Desea jugar otra vez? S / N: ")
        while otroJugador != 's' and otroJugador != 'S' and otroJugador != 'n' and otroJugador != 'N':
            otroJugador = input("¿Desea jugar otra vez? S / N: ")

        if otroJugador == 'n' or otroJugador == 'N':
            continuar = False

print()
print("Hasta luego")




    