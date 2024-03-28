'''
Banco necesita entregar la menor cantidad de billetes para un monto ingresado
Denominaciones: 1000,500,100,50,10,5,1
'''

importe = int(input("Ingrese el importe (sin decimales) a retirar: "))

mil = 0
quinientos = 0
cien = 0
cincuenta = 0
diez = 0
cinco = 0
uno = 0

if(importe//1000 > 0):
    mil += (importe//1000)
    importe -= (importe//1000)*1000
if(importe//500 > 0):
    quinientos += (importe//500)
    importe -= (importe//500)*500
if(importe//100 > 0):
    cien += (importe//100)
    importe -= (importe//100)*100
if(importe//50 > 0):
    cincuenta += (importe//50)
    importe -= (importe//50)*50
if(importe//10 > 0):
    diez += (importe//10)
    importe -= (importe//10)*10
if(importe//5 > 0):
    cinco += (importe//5)
    importe -= (importe//5)*5
if(importe//1 > 0):
    uno += importe
    importe -= importe//1

print('Billetes utilizados:')
print(" 1000: %d \n 500: %d \n 100: %d \n 50: %d \n 10: %d \n 5: %d \n 1:%d" % (mil,quinientos,cien,cincuenta,diez,cinco,uno))
