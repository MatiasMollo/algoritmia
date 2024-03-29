'''
Leer un numero correspondiente a un año e informar si es bisiesto o no
Nota: para ser bisiesto debe poder dividirse por 4,
no pueden dividirse por 100 a menos que también sean divisibles por 400
'''

year = int(input("Ingrese el año: "))

if(year%4==0 and (year%100!=0 or (year%100==0 and year%400==0))):
    print('El año es bisiesto')
else:
    print("El año no es bisiesto")