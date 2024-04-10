'''
Elegir tabla de multiplicar, ejemplo del 1 al 12 con el numero 4
'''



while True:
    numero = int(input("Ingrese el numero del cual desea consultar la tabla. -1 para finalizar: "))

    if str(numero) == '-1':
        break
    minimo = int(input("Ingrese el numero de comienzo de tabla: "))
    maximo = int(input("Ingrese el numero de fin de tabla: "))
    if minimo > maximo:
        print("Incoherencia en los datos, intente nuevamente")
    
    while minimo <= maximo:
        multiplicacion = numero*minimo
        print(numero,"x", minimo , ': ',multiplicacion)
        minimo += 1

    