'''
Realizar un programa que pida 10 numeros y muestre el promedio
'''

limite = 10
contador = 0
acumulador = 0

while contador < limite:
    contador += 1
    acumulador += float(input("Ingrese un número: "))

promedio = acumulador / limite

print("Promedio:",promedio)

'''
B) Detalle: El programa pide 10 números y los va sumando, cuando termina el ingreso, calcula el 
promedio dividiendo la suma total con la cantidad de números ingresados (en este caso 10).
Luego imprime el resultado del promedio

C) Los datos de entrada solo son números de tipo flotante, pueden ser positivos, negativos o cero
La salida es la variable Promedio

D) Las variables utilizadas son 'limite', usada para definir cuantas iteraciones hará el ciclo, 
'contador', la cual se incrementa con cada iteración y se compara contra la variable
'limite' para saber cuando finalizar el ciclo. 'acumulador', la cual es usada para sumar
todos los números que se ingresan y 'promedio', está ultima se obtiene de dividir la variable
'suma' con 'limite'

E) El resultado del programa es un promedio de todos los números ingresados

'''