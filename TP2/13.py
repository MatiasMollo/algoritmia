'''
Ingresar un numero binario de 4 cifras (se ingresa como numero entero) y transformarlo a decimal
'''

binario = input('Ingrese el numero binario de 4 digitos: ')
decimal = 0

if(len(binario) == 4):
    # Damos vuelta la palabra/numero con binario[::-1]
    for index,numero in enumerate(binario[::-1]):
        decimal += int(numero)*(2**int(index))

    print("El numero ingresado es: " + str(decimal))
else: print("El numero ingresado tiene mas de 4 digitos")