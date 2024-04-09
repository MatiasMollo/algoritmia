'''
Cuantos autos circulan con patente con numeración par y cuantos con impar en un día.
Escribir un programa que permita ingresar la terminación de la patente (0-9) hasta 
ingresar -1 e informar cuantos vehiculos pasaron con cada una de las cualidades mencionadas
'''
patente = 0
par = impar = 0

while True:
    if patente == -1:
        break
    patente = int(input("Ingrese la terminación de la patente, escriba -1 para finalizar: "))

    if patente >= 0 and patente <= 9:
        if patente%2==0: par += 1
        else: impar += 1
    else: 
        print("Incoherencia en los datos, intente nuevamente")

print("Patentes pares: %d \nPatentes impares: %d" % (par,impar))