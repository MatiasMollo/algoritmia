'''
Gestionar el inventario de una tienda de música, el usuario ingresa info de los instrumentos
(nombre, cantidad y precio).

El usuario ingresa múltiples instrumentos uno tras otro, finaliza cuando el nombre del mismo
es "fin"

Al finalizar la carga mostrar:
- Instrumentos totales
- Instrumento mas barato y su precio
- Instrumento mas caro y su precio
- Promedio de precio de todos los instrumentos
- Lista de instrumentos con menos de 5 unidades en stock
'''

instrumento = input("Ingrese el nombre del instrumento: ")
nombre_caro = False
nombre_barato = 0
precio_caro = 0
precio_barato = 0
total_instrumentos = 0
total_precios = 0

escasos = ''

while instrumento != 'fin':
    cantidad = int(input("Ingrese el stock del instrumento: "))
    precio = float(input("Ingrese el precio del instrumento: "))

    if cantidad > 0 and precio > 0:
        if total_instrumentos == 0:
            nombre_caro = nombre_barato = instrumento
            precio_caro = precio_barato = precio

        if cantidad < 5:
            escasos += instrumento + " "

        if precio < precio_barato:
            precio_barato = precio
            nombre_barato = instrumento
        
        if precio > precio_caro:
            precio_caro = precio
            nombre_caro = instrumento
        
        total_instrumentos += 1
        total_precios += precio
        print()
        instrumento = input("Ingrese el nombre del instrumento: ")
    else:
        print("Datos incorrectos, ingresar nuevamente.")

if total_instrumentos != 0:
    promedio = total_precios / total_instrumentos
    print()
    print("Cantidad total de articulos: ",total_instrumentos)
    print("Instrumento más caro:",nombre_caro,'con un precio de',precio_caro)
    print("Instrumento más barato:",nombre_barato,'con un precio de',precio_barato)
    print("El promedio de precios es:",promedio)
    print("Instrumentos con menos de 5 unidades:",escasos)
else:
    print("No se han ingresado datos")