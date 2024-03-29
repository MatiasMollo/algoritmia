'''
Se vota una ley en el congreso, hacer un programa que permita saber la cantidad de votos
a favor y en contra, e informe el porcentaje y si la ley fue aprobada o no
'''

# Para que se apruebe una ley, deben votar a favor mas de la mitad de los presentes
presentes = int(input("Ingrese el numero de diputados presentes: "))
favor = int(input("Ingrese la cantidad de votos a favor: "))
contra = int(input("Ingrese la cantidad de votos en contra: "))
abstenciones = presentes - (favor + contra)
aprobado = False

if (favor > presentes or contra > presentes or abstenciones > presentes or presentes < 0 or favor < 0 or contra < 0 or abstenciones < 0):
    print("Incoherencia en los datos. Intente nuevamente")
else:
    if(favor > presentes/2):
        print('Ley aprobada')
    else:
        print('Ley no aprobada')
        
    print('Porcentajes \n A favor: %d%% \n En contra: %d%% \n Abstenciones: %d%%' % (favor*100/presentes,contra*100/presentes,abstenciones*100/presentes))

