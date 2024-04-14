'''
Empresa aplica precio base a las primeras 12 unidades, entre la 13 y la 100
aplica 10% de descuento, mas de 100 aplica 25%.
Escribir un programa que lea la cantidad solicitada de un producto y su
precio base. Y muestre el precio promedio por unidad y el valor total de la venta.

Finalizar la carga ingresando -1 como cantidad solicitada. Imprimir la cantidad de ventas
en total, las ventas a las que se les aplico el 10% y cantidad que SOLO se le aplico el base
'''

cantidad = diez = ventas = base = 0
contador = 1

while cantidad != -1:
    cantidad = cantidad_inicial = int(input("Ingrese la cantidad del producto N°" + str(contador) + ': '))
    if cantidad == -1: precio = 0
    else: precio = float(input("Ingrese el precio base del producto N°" + str(contador) + ": "))
    precio_final = 0

    if cantidad > 0 and precio > 0:
        ventas += cantidad
        contador += 1

        if cantidad > 12:
            #Los primeros 12 sin descuento
            precio_final += 12 * precio
            cantidad -= 12

            if cantidad > 88: # Supera los 100 en total (12 + 88 = 100)
                #10% a 88 productos, 25% al resto
                precio_final += precio*0.90*88 + precio*0.75 * (cantidad - 88)
            else: 
                #10% de descuento
                precio_final += precio*0.90 * cantidad 
                diez += 1
        else: #Sin descuento
            precio_final = cantidad * precio
            base += 1

        promedio = precio_final / cantidad_inicial
        print("Precio total: ",precio_final,"\nPrecio promedio por producto: ",promedio)

print("Cantidad de ventas realizadas: ",ventas)
print("Cantidad de ventas solo con 10%: ",diez)
print("Cantidad de ventas sin descuento: ",base)
        