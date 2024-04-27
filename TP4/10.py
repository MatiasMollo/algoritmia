'''
Desarrollar un programa que calcule el factorial de un numero ingresado
'''

iteracion = False
num = int(input("Ingrese el número (0 para finalizar): "))
acumulador = 1
contador = 1

while not iteracion and num != 0:

    if(num > 0):
        iteracion = True
        while contador <= num:
            acumulador *= contador
            contador += 1

    else:
        print("Datos incorrectos, intente nuevamente")
        num = int(input("Ingrese el número: "))

if iteracion:
    print("Factorial: ", acumulador)
else:
    print("No se han ingresado datos válidos")
