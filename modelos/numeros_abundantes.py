# Determinar si el número ingresado es abundante, para esto la suma de sus divisores debe ser mayor al número ingresado

acumulador = 0
contador = 1
num = int(input("Ingrese su número: "))

if num > 0:
    while contador < num:
        if num%contador==0:
            acumulador += contador
        contador += 1
    if acumulador > num:
        print("El número es abundante")
    else:
        print("El número no es abundante")
else:
    print("El número debe ser positivo")
    