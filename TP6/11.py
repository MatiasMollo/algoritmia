'''
Obtener el dígito central de un número entero ingresado, solo si la
cantidad de dígitos es impar, si la longitud es impar devolver -1
'''

numero = int(input("Ingrese un número: "))
original = numero
digito = 0
contador_digitos = 0
posicion = 0
contador = 0

while numero != 0:
    contador_digitos += 1
    numero //= 10

numero = original

if contador_digitos % 2 != 0:
    posicion = (contador_digitos + 1) / 2
    while contador < posicion:
        digito = numero % 10
        numero //= 10
        contador += 1
    print("El dígito central es:",digito)
else:
    print("-1")