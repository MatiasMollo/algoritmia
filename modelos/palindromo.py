'''
Determinar si un número ingresado es palindromo o no
'''

original = int(input("Ingrese un número: "))
numero = original
aux = ''

while numero != 0:
    aux += str(numero%10) # Obtenemos el último dígito, se lo sumamos a modo de string por si es 0
    numero = numero//10 # Eliminamos el último dígito del número

if aux == str(original):
    print("El número es palíndromo")
else:
    print("El número no es palíndromo")