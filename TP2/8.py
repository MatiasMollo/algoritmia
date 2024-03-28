'''
Leer una medida en metros e imprimirla en centimetros, pulgadas, pied y yardas
'''

metros = float(input("Ingrese la medida en metros: "))

centimetros = metros*100
pulgadas = centimetros/2.54
pies = pulgadas/12
yardas = pies/3

print("Medidas \n Centimetros: " + str(centimetros) + "\n Pulgadas: " + str(pulgadas) + "\n Yardas: " + str(yardas) + "\n Pies: " + str(pies))
