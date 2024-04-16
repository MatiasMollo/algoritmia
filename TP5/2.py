'''
Ingresar numeros de legajo y nota de exámen final
Terminar la carga con -1 en el legajo
Informar si el alumno aprobó o no el exámen (se aprueba con 4). 
La nota debe estar entre 1 y 10
Al finalizar la carga informar cuantos aprobaron, cuantos desaprobaron
y el porcentaje de alumnos aplazados (1)
'''

legajo = nota = aprobados = aplazados = contador = 0

while legajo != -1:
    legajo = int(input("Ingrese N° de legajo: "))

    if legajo != -1:
        nota = int(input("Ingrese nota del alumno: "))
        if nota >= 1 and nota <= 10:
            if nota >= 4: 
                aprobados += 1
                print("Alumno ",legajo,': Aprobado')
            else:
                print("Alumno ",legajo,': Desaprobado')
                if nota == 1: aplazados += 1

            contador += 1

        else: print("Nota inválida, cargue nuevamente al alumno")


desaprobados = contador - aprobados
aplazados = aplazados * 100 / contador

print("\nAlumnos aprobados: ", aprobados)
print("Alumnos desaprobados: ", desaprobados)
print("Porcentaje de alumnos aplazados: ", aplazados)
