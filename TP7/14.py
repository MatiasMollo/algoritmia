'''
Leer número de legajo, fecha de nacimiento (dia, mes, año) de cada alumno
La carga finaliza cuando el legajo es -1.
Emitir un informe donde aparezca mes por mes cuantos alumnos cumplen a lo largo de todo
el año.
Indicar cual es el mes con mayor cantidad de cumpleaños
'''

legajo = int(input("Ingrese el número de legajo (-1 para finalizar): "))
alumnos = []

#Matriz para almacenar los meses con los cumpleaños
meses_cumple = []
for i in range(12):
    meses_cumple.append(0)

#Verifica que el legajo no se repita
def legajo_unico(legajo,alumnos):
    i = 0
    valid = True

    while i < len(alumnos) and valid:
        if alumnos[i] == legajo:
            valid = False
        i += 1

    return valid

#Verifica que la fecha ingresada sea válida
def validate_date(d,m,y):
    valid = True
    if d < 1 or m > 12 or m < 1:
        valid = False
    elif (m == 4 or m == 6 or m == 9 or m == 11) and d > 30:
        valid = False
    elif m == 2 and ((y%4==0 and (y%100!=0 or (y%100==0 and y%400==0)) and d > 29) or (d > 28)):
        valid = False
    elif d > 31:
        valid = False

    return valid

while legajo != -1:
    d = int(input("Ingrese el día: "))
    m = int(input("Ingrese el mes: "))
    y = int(input("Ingrese el año: "))

    if legajo_unico(legajo,alumnos) and validate_date(d,m,y):
        alumnos.append(legajo)
        meses_cumple[m-1] += 1 #Suma al contador de cumpleaños en el mes correspondiente
    else:
        print("Los datos son incorrectos o el legajo ya fue ingresado, intente nuevamente.")

    legajo = int(input("Ingrese el número de legajo (-1 para finalizar): "))
        
if len(alumnos):
    print()
    print("Cumpleaños por cada mes")
    mayor = 0
    cantidad_mayor = 0
    for i in range(12):
        print("Mes N°",i + 1,':',meses_cumple[i])

        if mayor == 0:
            mayor = i
            cantidad_mayor = meses_cumple[i]
        elif cantidad_mayor < meses_cumple[i]:
            cantidad_mayor = meses_cumple[i]
    print()
    print("El mes con mas cumpleaños fue el N°",mayor + 1,'con un total de ',cantidad_mayor,'cumpleaños')
else:
    print("No se han cargado alumos")