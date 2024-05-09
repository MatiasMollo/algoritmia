'''
Extraer un dígito de un número. La función recibe como parametros 2 numeros enteros,
uno es el numero (con todos sus digitos) y la última es que cifra se desea obtener.

Ejemplo: extraerDigito(12345,1) devuelve 4
'''

def extraerDigito(numero,digito = 0):
    ret = -1
    longitud = len(str(numero))
    if numero < 0:
        longitud -= 1

    if digito < longitud:
        ret = str(numero)[len(str(numero)) - digito - 1]
    return ret

numero = int(input("Ingrese el número entero: "))
digito = int(input("Ingrese la cifra que desea obtener: "))

print("El dígito solicitado es:",extraerDigito(numero,digito))