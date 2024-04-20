'''
Complejo de cines, se ingresa la cantidad de espectadores por cada función
espectadores = 0 -> Se termina la carga
por cada funcion se ingresa si tiene descuento (1 = si, 2 = no)

Calcular recaudación del complejo, la entrada sale $3500 con descuento, $5000 sin desc.
Determinar cuatos espectadores ingresaron con descuento y que porcentaje representan
sobre el total de funciones
'''

ENTRADA = float(input("Ingrese el valor de la entrada: "))
ENTRADA_DESC = float(input("Ingrese el valor de la entrada con descuento: "))
recaudacion = 0
cant_espectadores = 0
cant_espectadores_desc = 0

print()
espectadores = int(input("Ingrese la cantidad de espectadores: "))

#Validamos que los espectadores sean mayores que 0, caso contrario se corta la ejecución
while espectadores > 0:
    descuento = int(input("Ingrese 1 si la función tiene descuento, en caso contrario ingrese 2: "))
    
    if descuento == 1:
        cant_espectadores_desc += espectadores
        recaudacion += espectadores*ENTRADA_DESC
    elif descuento == 2:
        cant_espectadores += espectadores
        recaudacion += espectadores*ENTRADA
    else:
        print("Operación inválida, intente nuevamente")

    espectadores = int(input("Ingrese la cantidad de espectadores: "))

#Si al principio del programa ingresamos 0, se divide por 0 y revuelve una excepción
if cant_espectadores > 0 or cant_espectadores_desc > 0:
    porcentaje_espectadores_desc = cant_espectadores_desc * 100 / (cant_espectadores_desc + cant_espectadores)
else:
    porcentaje_espectadores_desc = 0

print()
print("Recaudación total: $",recaudacion)
print("Cantidad de espectadores con descuento: ",round(cant_espectadores_desc,2))
print("Porcentaje de espectadores con descuento: %",porcentaje_espectadores_desc)