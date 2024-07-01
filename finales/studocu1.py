'''
Pago mensual a los proveedores las facturas del mes anterior, si la factura es abonada despues del dia 20 se ha acordado un extra del 15% sobre el valor de la factura

El empleado tendrá a cargo la siguiente información:
- Código de proveedor
- Nro factura
- Día de pago
- Importe de factura

La carga finaliza al ingresar -1 en codigo de proveedor.
Mostrar un listado ordenado por día de forma ascendente especificando también cual es el importe y de cuanto es el total (con el extra)

Utilizar listas enlazadas y el algoritmo de burbujeo
'''
#Copia una lista ya que python solo guarda el puntero de memoria al realizar lista1 = lista2
def copiar(lista):
    array = []

    for i in range(len(lista)):
        array.append(lista[i])

    return array

#Retorna True si la factura NO está repetida
def validarFactura(factura,facturas):
    repetida = False
    i = 0

    if factura == '':
        repetida = True

    while not repetida and i < len(facturas):
        if factura == facturas[i]:
            repetida = True
        i += 1
    
    return not repetida

#Devuelve los indices para imprimir las listas, decidí devolver una lista de indices para no ordenar las variables de forma global
def ordenar(dias):
    lista = copiar(dias)
    indices = []
    ordenado = False
    aux = 0

    while not ordenado:
        ordenado = True

        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                ordenado = False
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux

    for i in range(len(dias)):
        for x in range(len(lista)):
            if dias[i] == lista[x]:
                indices.append(x)

    return indices

def calcularTotales(dias,importes,interes,dias_interes):
    totales = []
    total = 0
    for i in range(len(dias)):
        if dias[i] >= dias_interes:
            total = importes[i] * (1+interes/100)
        else:
            total = importes[i]
        totales.append(total)
    
    return totales


#Programa principal
codigos = []
facturas = []
dias = []
importes = []


INTERES = 15 #Porcentaje de internet
DIAS_INTERES = 20 #Dias desde donde se empieza a cobrar el interes

codigo = input("Ingrese el código proveedor (-1 para finalizar): ")

while codigo != '-1':

    while codigo == '':
        codigo = input("Código no válido, intente nuevamente: ")

    factura = input("Ingrese el N° de factura: ")
    while not validarFactura(factura,facturas): #Verifica que la factura no se repita
        factura = input("Esa factura ya fue ingresada, intente nuevamente: ")

    dia = int(input("Ingrese el día de pago: "))
    while dia < 1 or dia > 31:
        dia = int(input("Dato incorrecto, intente nuevamente: "))

    importe = float(input("Ingrese el importe de la factura: "))

    while importe <= 0:
        importe = float(input("El importe debe ser superior a $0, intente nuevamente: "))
    
    codigos.append(codigo)
    facturas.append(factura)
    dias.append(dia)
    importes.append(importe)

    print("Factura cargada correctamente")
    print()

    #Final
    codigo = input("Ingrese el código proveedor (-1 para finalizar): ")

print("Ha finalizado la carga")


if len(codigos) > 0:
    ordenado = ordenar(dias)
    totales = calcularTotales(dias,importes,INTERES,DIAS_INTERES)

    print()
    print("Proveedor | N° factura | Día de pago | Importe | Total")
    for i in range(len(ordenado)):
        print(codigos[ordenado[i]],' | ',facturas[ordenado[i]],' | ',dias[ordenado[i]],' | ', importes[ordenado[i]],' | ', totales[ordenado[i]])
else:
    print("No se han ingresado facturas")