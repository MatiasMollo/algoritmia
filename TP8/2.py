'''
Cobro de las expensas de un edifiio, departamentos de 20 unidades.
En dos listas se almacena N° de unidad y superficie en M2

Validar que no se ingresen N° de unidades duplicadas. Cada unidad paga un valor fijo en 
relacion con su tamaño (se ingresa por teclado)

Se pide:
- Informar el promedio de expensas del mes
- Ordenar los listados de mayor a menor según la superficie. Mostrar por pantalla
    la lista ordenada informando el N° de unidad y su superficie
'''

CANTIDAD_DEPARTAMENTOS = 4

#Verifica que la unidad no esté repetida en el listado. Devuelve V si la unidad no se encuentra
def validarUnidad(unidad, departamentos):
    i = 0
    repetido  = False

    while not repetido and i < len(departamentos):
        if departamentos[i] == unidad:
            repetido = True 
        i += 1

    return not repetido

# Devuelve una lista con los indices ordenados en base a la superficie del Dto.
def ordenar(departamentos,superficies):
    lista = []
    ordenado = False
    original = departamentos
    aux = 0

    while not ordenado:
        ordenado = True
        for i in range(len(departamentos)-1):
            if(superficies[i] > superficies[i+1]):
                aux = departamentos[i]
                departamentos[i] = departamentos[i+1]
                departamentos[i+1] = aux

                aux = superficies[i]
                superficies[i] = superficies[i+1]
                superficies[i+1] = superficies[i]
                ordenado = False
    
    #Ordenado de indices
    for i in range(len(departamentos)):
        for x in range(len(departamentos)):
            if departamentos[i] == original[x]:
                lista.append(i)

    return lista

def promedio(superficies,valor):
    suma = 0

    for i in range(len(superficies)):
        suma += superficies[i] * valor
    
    return suma / len(superficies)
        

# Programa principal
departamentos = []
superficies = []

valor = float(input("Ingrese el precio del M2: "))
while valor < 0:
    valor = float(input("Valor incorrecto, intente nuevamente: "))

for i in range(CANTIDAD_DEPARTAMENTOS):
    print()
    unidad = int(input("Ingrese el N° de unidad: "))
    while not validarUnidad(unidad,departamentos):
        unidad = int(input("Esa unidad ya fue ingresada, intente nuevamente: "))

    metros = float(input("Ingrese los M2 de la unidad: "))
    while metros < 0:
        metros = float(input("El valor no puede ser negativo, intente nuevamente: "))

    departamentos.append(unidad)
    superficies.append(metros)

print()
listado = ordenar(departamentos,superficies)

print("Listado de departamentos: \n")
for i in range(len(listado)):
    print("- N°",departamentos[listado[i]],"con",superficies[listado[i]],"M2")

importePromedio = promedio(superficies,valor)

print()
print("El valor promedio de las expensas es de: $",importePromedio)