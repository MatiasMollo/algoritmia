'''
Empresa factura a sus clientes el último dia de cada mes.
Si el cliente paga dentro de los primeros 10 dias tiene un descuento de 200 o 2%, lo 
que resulte mas conveniente para el cliente.
Si paga en los próximos 10 dias (del 10 al 20) se le cobra el importe original.
Si paga en los últimos 10 dias del mes deberá abonar una multa de 350 o 10% de su 
factura (lo que resulte mayor)

Inputs: N° cliente y total de la factura
Emitir informe con las opciones e importes de pago
'''

cliente = 0

DESCUENTO_EFECTIVO = 200
DESCUENTO_PORCENTAJE = 0.02
MULTA_EFECTIVO = 350
MULTA_PORCENTAJE = 0.10

contador = 1

while cliente != -1:
    factura = float(input("Ingrese la factura del cliente N°" + str(contador) + ": "))
    if factura > 0:
        contador += 1