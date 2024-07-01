'''
Pago mensual a los proveedores las facturas del mes anterior, si la factura es abonada despues del dia 20 se ha acordado un extra del 15% sobre el valor de la factura

El empleado tendrá a cargo la siguiente información:
- Nro factura
- Día de pago
- Importe de factura

La carga finaliza al ingresar -1 en codigo de proveedor.
Mostrar un listado ordenado por día de forma ascendente especificando también cual es el importe y de cuanto es el total (con el extra)
'''

DIAS = 20
INTERES = 15

def copiar(lista):
    array = []
    for i in range(len(lista)):
        array.append(lista[i])
    return array

def getIndices(lista,ordenados):
    array = []

    for i in range(len(lista)):
        for x in range(len(ordenados)):
            if lista[i] == ordenados[x]:
                array.append(x)
    return array

def burbuja(dias):
    dias = copiar(dias)
    ordenado = False
    
    while not ordenado:
        ordenado = True
        for i in range(len(dias)-1):
            if dias[i] > dias[i+1]:
                ordenado = False
                aux = dias[i]
                dias[i] = dias[i+1]
                dias[i+1] = aux

    return dias

def insercion(dias):
    dias = copiar(dias)
    for i in range(1,len(dias)):
        x = i
        aux = dias[i]

        while x > 0 and dias[x-1] > aux:
            dias[x] = dias[x-1]
            dias[x-1] = aux
            x -= 1

    return dias

def seleccion(dias):
    dias = copiar(dias)
    
    for i in range(len(dias)-1):
        for x in range(i,len(dias)):
            if dias[i] > dias[x]:
                aux = dias[i]
                dias[i] = dias[x]
                dias[x] = aux
    return dias

def calcularInteres(importes,dias):
    totales = []

    for i in range(len(importes)):
        if dias[i] >= DIAS:
            importe = importes[i]*(1+INTERES/100)
        else:
            importe = importes[i]
        totales.append(importe)

    return totales

#Programa principal
facturas = []
dias = []
importes = []

factura = input("Ingrese un número de factura (-1 para finalizar): ")

while factura != '-1':
    while factura == '':
        factura = input("Factura no válida, intente nuevamente: ")

    dia = int(input("Ingrese el día de pago: "))
    while dia < 1 or dia > 31:
        dia = int(input("Día inválido, intente nuevamente: "))
    
    importe = float(input("Ingrese el importe de la factura: "))
    while importe <= 0:
        importe = float(input("Importe inválido, intente nuevamente: "))

    facturas.append(factura)
    dias.append(dia)
    importes.append(importe)

    print()
    factura = input("Ingrese un número de factura (-1 para finalizar): ")


if len(facturas) > 0:
    print()
    ordenados = getIndices(dias,burbuja(dias))
    totales = calcularInteres(importes,dias)
    print("Array dias:",dias)
    print("burbuja:",ordenados)
    print('inserción:',getIndices(dias,insercion(dias)))
    print('selección:',getIndices(dias,seleccion(dias)))

    print()
    for i in range(len(ordenados)):
        print("Factura N°",facturas[ordenados[i]],"día",dias[ordenados[i]],'importe:',importes[ordenados[i]],'- total:',round(totales[ordenados[i]],2))

else:
    print("No se han ingresado facturas")