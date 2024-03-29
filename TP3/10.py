'''
Calcular y mostrar el sueldo neto de un empleado en base a su sueldo básico y su antigüedad
en años.
Si es soltero se incrementa en un 5% el salario bruto por cada año de antigüedad, si es 
casado se incrementa un 7% bruto por cada año de antigüedad.
Se le realizan los descuentos del 11% de jubilación, 3% de obra social y 3% de sindicato

Inputs: Sueldo básico, antigüedad y estado civil.
Outputs: Sueldo básico, antigüedad, jubilación, obra social, sindicato y sueldo neto
'''

basico = float(input('Ingrese el sueldo básico: $'))
old = int(input("Ingrese los años de antigüedad: "))
estado = int(input("Ingrese estado civil (1 para soltero, 2 para casado): "))

sueldo = 0

if(estado == 1):
    sueldo = basico*((1.05)**old)
elif (estado == 2):
    sueldo = basico*((1.07)**old)

jubilacion = sueldo*0.11
obra_social = sindicato = sueldo*0.03


print("Básico: $%.2f \nAntigüedad: %d años. Importe: $%.2f \nJubilación: -$%.2f \nObra social: -$%.2f \nSindicato: -$%.2f \nSueldo Neto: $%.2f" % (basico,old,sueldo - basico,jubilacion,obra_social,sindicato,(sueldo-(jubilacion+obra_social+sindicato))))