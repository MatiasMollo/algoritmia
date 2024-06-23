'''
Prueba de probabilidades para tecnica de la rulleta en donde solo se pierde si sale un número menor o igual a 6
'''

import random

# dinero = float(input("Ingrese la cantidad de dinero con la que jugará: "))
escenarios = int(input("Ingrese la cantidad de escenarios a probar: "))
tiradas = int(input("Ingrese la cantidad de tiradas por escenario: "))

while escenarios < 1 or tiradas < 1:
    print("Los datos son inválidos, intente nuevamente")  
    # dinero = float(input("Ingrese la cantidad de dinero con la que jugará: "))
    escenarios = int(input("Ingrese la cantidad de escenarios a probar: "))
    tiradas = int(input("Ingrese la cantidad de tiradas por escenario: "))

#Rompe el ciclo while cuando se pierde la tirada
salirAlPerder = input("¿Desea finalizar el escenario cuando se pierda una tirada? S / N: ")
dinero = 5000

contador = 0
valorPorTirada = 500
ganancia = 100

ganadas = 0
perdidas = 0
empatadas = 0

while contador < escenarios:
    tirada = 0
    saldo = dinero

    while  tirada < tiradas and saldo >= valorPorTirada:
        numero = random.randint(0,36)

        if numero <= 6:
            saldo -= valorPorTirada
            if salirAlPerder == "S" or salirAlPerder == "s":
                print("numero",numero,"saldo:",saldo)
                break
        else:
            saldo += ganancia

        print("numero",numero,"saldo:",saldo)
        tirada += 1

    if saldo > dinero:
        ganadas += 1
    elif saldo < dinero:
        perdidas += 1
    else:
        empatadas += 1
    contador += 1
    print("-----------------------------")
    print("Escenario",contador,":",saldo)
    print("-----------------------------")
    print()


print()
print("Escenarios con saldo positivo:",ganadas)
print("Escenarios con saldo negativo:",perdidas)
print("Escenarios empatados:",empatadas)

'''
CONCLUSIONES:

Al realizar muchas tiradas por escenario, por mas que salga apenas se pierde una, los resultados finales son negativos.
No obstante, al probar muchos escenarios con pocas tiradas (2) y sin salir apenas se pierde, los resultados son positivos
(69 positivos, 31 negativos). Alrededor de 70% de probabilidades de ganar

Evaluando en 100 escenarios con 3 tiradas por cada uno, el porcentaje de ganar al final del juego se transforma en 50%

Al evaluar 100 escenarios con 1 sola tirada en cada uno, las probabilidades de ganar aumentan a 80% aprox

'''