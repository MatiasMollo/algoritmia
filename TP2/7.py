'''
Una persona invierte su dinero en un banco, este mismo paga un interes de 2% mensual
¿Cuanto gana en 6 meses invertido?
'''

dinero = round(float(input("Ingrese la cantidad de dinero a depositar: $")),2)
interes_mensual = 2
meses = 6

dinero_futuro = round(dinero*((1 + interes_mensual/100)**meses),2)

print("El dinero dentro de 6 meses será $" + str(dinero_futuro) + ", Habiendo ganado un total de $" + str(round(dinero_futuro - dinero,2)))