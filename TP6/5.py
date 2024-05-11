'''
Desarrollar la función signo(n), recibe un número entero y devuelve 1, -1 o 0 según el 
valor recibido sea positivo, negativo o nulo.
'''

def signo (numero):
    signo = 0
    if numero > 0:
        signo = 1
    elif numero < 0:
        signo = -1
    return signo

print("Devolución: ",signo(int(input("Ingrese un número: "))))