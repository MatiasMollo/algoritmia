'''
Inmobiliaria paga a vendedores $250.000, comision de $5.000 y el 5% del valor de las ventas. 
Imprimir el numero de vendedor y salario que le corresponde en un determinado mes.
Inputs: numero de vendedor, cantidad de ventas que realizó y el valor total de las mismas
'''

cantidad_vendedores = int(input("Ingrese la cantidad de vendedores a cargar: "))
vendedores = []
sueldo_base = 250000
comision_por_venta = 5000
porcentaje = 5

for vendedor_index in range(cantidad_vendedores):
    print()
    cantidad_ventas = int(input("Ingrese el numero de ventas del vendedor N°" + str(vendedor_index + 1) + ': '))
    ventas = []

    for venta_index in range(cantidad_ventas):
        ventas.append(float(input('Valor de la venta N°' + str(venta_index + 1) + ': ')))
    
    vendedores.append(ventas)

print()

for index,vendedor in enumerate(vendedores):
    sueldo = sueldo_base

    for i,venta in enumerate(vendedor):
        sueldo += comision_por_venta + venta*(porcentaje/100)

    print('Sueldo vendedor N°' + str(index + 1) + ': $' + str(sueldo))