'''
N empleados, categorias 1 2 y 3, por cada uno se lee su legajo, categoria y salario

Elaborar un informe que contenga:
- Importe total de salarios pagados por la empresa
- Cantidad de empleados que ganan mas de 200k
- Cantidad de empleados que ganan menos de 50k cuya categoria sea 3
- Legajo del empleado q mas gana
- Sueldo mas bajo
- Importe total de sueldos por cada categoria
- Salario promedio

Suposicion: El programa termina al ingresar 0 como legajo
'''

legajo = int(input("Ingrese legajo del empleado: "))
contador = 0
total_sueldos = 0
mas_200 = 0
menos_50 = 0
sueldo_alto = 0
empleado_mas_gana = 0
sueldo_bajo = 0
importes_cat_1 = 0
importes_cat_2 = 0
importes_cat_3 = 0


while legajo != 0:
    categoria = int(input("Ingrese la categoria (1,2 o 3): "))
    salario = float(input("Ingrese el salario del empleado: "))

    if salario < 0 or categoria < 1 or categoria > 3:
        print("Datos incorrectos, intente nuevamente.")
    else:
        if contador == 0:
            sueldo_alto = sueldo_bajo = salario
            empleado_mas_gana = legajo

        total_sueldos += salario
        contador += 1

        if categoria == 1:
            importes_cat_1 += salario
        elif categoria == 2:
            importes_cat_2 += salario
        else:
            importes_cat_3 += salario
            if salario < 50000:
                menos_50 += 1
        
        if salario > 200000:
            mas_200 += 1

        if salario > sueldo_alto:
            sueldo_alto = salario
            empleado_mas_gana = legajo
        if salario < sueldo_bajo:
            sueldo_bajo = salario
        
        print()
        legajo = int(input("Ingrese legajo del empleado: "))

if contador > 0:
    promedio = total_sueldos / contador
    print()
    print("Total pagado por la empresa:",total_sueldos)
    print("Cantidad de empleados que ganan mas de 200k: ",mas_200)
    print("Cantidad empleados de categoria 3 con sueldo menor a 50000:",menos_50)
    print("Empleado que mas gana:",empleado_mas_gana,'con un sueldo de',sueldo_alto)
    print("Sueldo mas bajo: ",sueldo_bajo)
    print("Importe sueldo categoria 1:",importes_cat_1)
    print("Importe sueldo categoria 2:",importes_cat_2)
    print("Importe sueldo categoria 3:",importes_cat_3)
    print("Salario promedio: ", promedio)   
else:
    print("No se han ingresado datos")
