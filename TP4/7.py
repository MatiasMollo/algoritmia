'''
Leer 10 numeros enteros e imprimir su promedio, el mayor valor leido, y en que posicion
se encontraba. Si se ingreso mas de una vez solo debe informar la primera
'''

LIMITE = 10

contador = 1
mayor = 0
posicion = 0
promedio = 0

while contador <= LIMITE:
    num = int(input("Ingrese un número: "))

    if contador == 0:
        mayor = num
        posicion = contador
    elif mayor < num:
        mayor = num
        posicion = contador
    
    contador += 1
    promedio += num

if contador > 0:
    promedio = promedio / LIMITE
    print("El promedio es",promedio,"su mayor número fue",mayor,"en la posicion",posicion)
else:
    print("El promedio no pudo ser calculado, reintente nuevamente")

