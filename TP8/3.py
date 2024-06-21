'''
Ciclista, participan N competidores (se ingresa por teclado).
Por cada competidor se carga su número y el tiempo en horas, minutos y segundos

Luego se solicita mostrar el número del ganador y su tiempo
Se pide ingresar por teclado un tiempo record y verificar que el ganador lo haya superado
Calcular y mostrar el tiempo promedio de todos los ciclistas
'''

#retorna Verdadero cuando un item se encuentra en un array
def esRepetido(item,lista):
    repetido = False
    i = 0
    while repetido == False and i < len(lista):
        if(item == lista[i]):
            repetido = True
        i += 1

    return repetido

#Devuelve una lista con el tiempo equivalente en segundos
def convertirSegundos(horas,minutos,segundos):
    return horas*60*60 + minutos*60 + segundos

def calcularPromedio(segundos):
    suma = 0
    for i in range(len(segundos)):
        suma += segundos[i]

    return suma / len(segundos)

#Devuelve la posición en donde se encuentra el ganador
def obtenerIndiceGanador(competidores,segundos):
    ganador = 0
    tiempo = 0

    for i in range(len(competidores)):
        if i == 0 or segundos[i] < tiempo:
            ganador = i
            tiempo = segundos[i]

    return ganador

#Programa principal
ciclistas = int(input("Ingrese la cantidad de ciclistas a cargar: "))
while ciclistas < 1:
    ciclistas = int(input("La cantidad no puede ser menor a 1, intente nuevamente: "))

competidores = []
horas = []
minutos = []
segundos = []

i = 0
while i < ciclistas:
    print()
    competidor = int(input("Ingrese el N° del competidor: "))
    while esRepetido(competidor,competidores):
        competidor = int(input("Ese competidor ya se ingresó, intente nuevamente: "))
    
    hora = int(input("Ingrese la cantidad de horas que demoró el competidor: "))
    minuto = int(input("Ingrese los minutos que demoró el competidor: "))
    segundo = int(input("Ingrese los segundos que demoró el competidor: "))

    if hora < 0 or minuto < 0 or segundo < 0:
        print("Las horas, minutos y segundos no pueden ser negativos, cargue al competidor nuevamente")
    else: 
        competidores.append(competidor)
        horas.append(hora)
        minutos.append(minuto)
        segundos.append(segundo)
        i += 1

tiempos = []
for i in range(len(horas)):
    tiempos.append(convertirSegundos(horas[i],minutos[i],segundos[i]))

indiceGanador = obtenerIndiceGanador(competidores,tiempos)
promedio = calcularPromedio(tiempos)

print()
record_horas = int(input("Ingrese el tiempo en horas del record: "))
record_minutos = int(input("Ingrese el tiempo en minutos del record: "))
record_segundos = int(input("Ingrese el tiempo en segundos del record: "))

while record_horas < 0 or record_minutos < 0 or record_segundos < 0:
    print("Los tiempos ingresados no pueden ser negativos, intente nuevamente.")
    print()
    record_horas = int(input("Ingrese el tiempo en horas del record: "))
    record_minutos = int(input("Ingrese el tiempo en minutos del record: "))
    record_segundos = int(input("Ingrese el tiempo en segundos del record: "))

record = convertirSegundos(record_horas, record_minutos,record_segundos)

print()
print("El ganador es el ciclista N°", competidores[indiceGanador],"con un tiempo de",tiempos[indiceGanador],"segundos")
if tiempos[indiceGanador] < record:
    print("El ganador superó el record anterior")
else:
    print("El ganador no superó el record anterior")

print()
print("El promedio de tiempo es de ",promedio,"segundos")
