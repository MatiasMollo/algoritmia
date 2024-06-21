'''
Leer N° de legajo de alumnos y su nota del examen final. La carga finaliza cuando se ingresa -1 como legajo
La nota debe estar entre 1 y 10

Luego informar:
- la cantidad de alumnos con nota >= 4
- Cantidad de alumnos desaprobados (>= 4)
- Promedio de nota y los legajos que superan el promedio
'''
# Retorna el estado del alumno en base al parametro booleano recibido
def estado(legajos,notas,aprobados):
    resultado = []
    for i in range(len(legajos)):
        if(notas[i] >= 4 and aprobados):
            resultado.append(legajos[i])
        elif not aprobados and notas[i] < 4:
            resultado.append(legajos[i])

    return resultado

def calcularPromedio(legajos,notas):
    promedio = 0
    for i in range(len(legajos)):
        promedio += notas[i]

    return promedio / len(notas)

def encimaPromedio(legajos,notas,promedio):
    resultado = []

    for i in range(len(legajos)):
        if(notas[i] >= promedio):
            resultado.append(legajos[i])

    return resultado

#Programa principal
legajos = []
notas = []

legajo = int(input("Ingrese el N° de legajo: "))

while legajo != -1:
    legajos.append(legajo)
    
    nota = float(input("Ingrese la nota númerica: "))

    while nota < 1 or nota > 10:
        nota = float(input("La nota debe estar comprendida entre 1 y 10: "))

    notas.append(nota)
    legajo = int(input("Ingrese el N° de legajo: "))

promedio = calcularPromedio(legajos,notas)
aprobados = estado(legajos,notas,True)
desaprobados = estado(legajos,notas,False)
alumnosEncimaPromedio = encimaPromedio(legajos,notas,promedio)

print()
print("----------------------------")
print("Aprobados:",aprobados)
print("Desaprobados:",desaprobados)
print("Promedio:",promedio,". Alumnos que superan el promedio:",alumnosEncimaPromedio)
print("----------------------------")
