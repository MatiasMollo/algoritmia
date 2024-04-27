'''
Leer un número entero e invertir las cifras que contiene
Imprimir por pantalla el número invertido. El mismo puede ser negativo
'''

numero = int(input("Ingrese un número: "))

negativo = False
digito = 0
numero_invertido = 0

if numero < 0:
    negativo = True
    numero = numero * -1

while numero != 0:
    digito = numero%10
    numero //= 10
    numero_invertido = numero_invertido*10 + digito

if negativo:
    numero_invertido *= -1

print("El número invertido es:",numero_invertido)