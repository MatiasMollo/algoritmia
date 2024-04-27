'''
Leer 3 números (D,M,A) correspondientes al dia, mes y año
Ingresar N (entero) e imprimir la fecha que resulta de sumar N a la fecha ingresada

'''

d = int(input("Ingrese un día (0 para finalizar): "))
contador = 0
bisiesto = False

while contador == 0 and d > 0:
    m = int(input("Ingrese un mes: "))
    a = int(input("Ingrese un año: "))

    if(a%4==0 and (a%100!=0 or (a%100==0 and a%400==0))):
        bisiesto = True

    #Validaciones para años bisiestos, excedente de dias, etc
    validaciones = (bisiesto and m == 2 and d <= 29) or (not bisiesto and m == 2 and d <= 28)
    d31 = (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12)
    d30 = (m == 4 or m == 6 or m == 9 or m == 11)
    validaciones = validaciones and ((d31 and d <= 31) or (d30 and d <= 30) or m == 2)

    if validaciones:
        contador += 1
        num = int(input("Ingrese la cantidad de días a sumar: "))

        if m == 2:
            if bisiesto:
                dias = 29
            else:
                dias = 28
        elif d31:
            dias = 31
        else:
            dias = 30

        d += num

        while d > dias:
            d -= dias
            m += 1
            if m > 12:
                m = 1
                a += 1
                
    else:
        print("Datos incorrectos, intente nuevamente")
        d = int(input("Ingrese un día: "))

if contador > 0:
    print("Nueva fecha:",d,'/',m,'/',a)
else:
    print("No se han ingresado fechas.")

