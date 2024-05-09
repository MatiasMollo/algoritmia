'''
Raiz cuadrada mediante formula de newton
detener el programa cuando la diferencia entre 2 calculos sea menor a 0,0001

Se debe calcular la raiz cuadrada de un número positivo
Utilizar como primera aproximación a (n/2)
'''

def calcular(n,a):
    return ((n/a) + a) / 2

numero = int(input("Ingrese un número: "))
aproximacion = numero / 2
resultado_anterior = aproximacion
diferencia = 1
resultado = 0
DIFERENCIA = 0.0001

if numero > 0:
    while diferencia > DIFERENCIA:
        resultado = calcular(numero,aproximacion)
        diferencia = aproximacion - resultado
        aproximacion = resultado

    print("Aproximación:",aproximacion)
else:
    print("El número debe ser positivo.")