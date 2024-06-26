'''
Ingresar un número N y construir una lista con N números enteros entre 1 y 20 en su interior
Luego, recorrer la lista y separar sus valores cuando la suma de mas de 20

Ejemplo
Numeros: 5,2,9,6,4
Lista: 5,2,9,0,6,4

#EJ7
A partir del EJ6 imprimir la secuencia mas larga almacenada en la misma.
Si hubiera varias secuencias con la misma longitud máxima imprimirlas
'''

import random

MINIMO = 1
MAXIMO = 20

def generar(numero,minimo,maximo):
    lista = []
    i = 0

    while i < numero:
        lista.append(random.randint(minimo,maximo))
        i += 1
    
    return lista

def separar(secuencia):
    lista = []
    suma = 0
    i = 0

    while i < len(secuencia):
        if suma + secuencia[i] > 20:
            suma = 0
            lista.append(0)
        else: 
            suma += secuencia[i]
            lista.append(secuencia[i])
            i += 1

    lista.append(0)
    return lista

#EJ7
def mayorLongitud(secuencia):
    longitud = 0
    mayor = 0
    i = 0

    for i in range(len(secuencia)):
        if secuencia[i] == 0:
            if longitud > mayor:
                mayor = longitud
            longitud = 0
        else:
            longitud += 1

    return mayor

#Devuelve todas las secuencias en forma de matriz que coinciden con la longitud pasada
def obtenerSecuencias(secuencia,longitud):
    lista = []
    listaCompleta = []

    for i in range(len(secuencia)):
        if secuencia[i] != 0:
            lista.append(secuencia[i])
        else:
            if len(lista) == longitud:
                listaCompleta.append(lista)
            lista = []

    return listaCompleta


#Programa principal
numero = int(input("Ingrese la cantidad de números a generar: "))
while numero < 1:
    numero = int(input("El número no puede ser menor a 1, intente nuevamente: "))

secuencia = generar(numero,MINIMO,MAXIMO)

print()
print("Secuencia")
print(secuencia)
secuencia = separar(secuencia)
print()
print("Secuencia separada")
print(secuencia)

print()
mayor = mayorLongitud(secuencia)
print("Mayor longitud:",mayor)

print()
print("Secuencias con la mayor longitud:")
lista = obtenerSecuencias(secuencia,mayor)
for i in range(len(lista)):
    print(i+1,"->",end=" ")
    for x in range(len(lista[i])):
        print(lista[i][x],end=" ")
    print()