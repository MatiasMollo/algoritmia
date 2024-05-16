'''
Escribir una función para contar cuantas veces aparece un número dentro de una lista, la función recibe la lista y el número a buscar
'''

def buscar(lista,elemento):
    contador = 0

    for i in range(len(lista)):
        if lista[i] == elemento:
            contador += 1

    return contador

lista = []
numero = int(input("Ingrese un número (-1 para finallizar): "))

while numero != -1:
    lista.append(numero)
    numero = int(input("Ingrese un número (-1 para finalizar): "))

elemento = int(input("Ingrese el número a buscar: "))

print("El número aparece",buscar(lista,elemento),"veces en la secuencia ingresada")