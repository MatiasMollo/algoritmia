'''
Crear una lista de N números generados al azar entre 0 y 100 pero sin elementos repetidos

Resolver utilizando 2 estrategias
- Impidiendo el agregado de elementos repetidos
- Eliminando los duplicados luego de generada la lista. Asegurarse que la cantidad final
de elementos sea la solicitada
'''

import random

MAX = 100
MIN = 0

# Devuelve True si el elemento ya se encuentra en la lista
def repetido(lista,numero):
    repetido = False
    for i in range(len(lista)):
        if lista[i] == numero:
            repetido = True
    return repetido

# Agrega el elemento mientras que no esté repetido
def agregar(cantidad):
    lista = []

    while len(lista) < cantidad:
        numero = random.randint(MIN,MAX)
        if not repetido(lista,numero):
            lista.append(numero)

    return lista

# Agrega el elemento, verifica si está repetido y lo borra en caso verdadero
def agregar_eliminando(cantidad):
    lista = []
    repetidos = []
    i = 0

    while (len(lista) - len(repetidos)) < cantidad:
        numero = random.randint(MIN,MAX)

        if repetido(lista,numero):
            repetidos.append(numero)

        lista.append(numero)
    
    while i < len(lista) and len(repetidos) > 0:
        if lista[i] == repetidos[0]:
            del(repetidos[0])
            del(lista[i])
        else:
            i += 1

    return lista

# Programa principal
cantidad = int(input("Ingrese la cantidad de números que tendrá la lista: "))
while cantidad < 1 or cantidad > 100:
    cantidad = int(input("Cantidad incorrecta, debe estar entre 0 y 100: "))

print("Lista con función agregar:",agregar(cantidad))
print("Lista con función agregar_eliminando:",agregar_eliminando(cantidad))
