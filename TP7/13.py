'''
Leer 2 listas de números y ordenarlos de menor a mayor. Luego se solicita generar e imprimir
una tercera lista que resulte de intercalar las primeras 2 (también debe quedar ordenada, sin
utilizar ningún método de ordenamiento en ella)
'''
def getList():
    leave = False
    array = []

    while not leave:
        numero = int(input("Ingrese un número (0 para finalizar): "))
        if numero == 0:
            leave = True
        else:
            array.append(numero)

    return array

def orderList(array):
    aux = 0
    for i in range(len(array)):
        for x in range(len(array)):
            if array[x] > array[i]:
                aux = array[i]
                array[i] = array[x]
                array[x] = aux
    return array

def mix(M,N): #Al intercalar, no se debe hacer de uno en uno, si no recorrer los arrays y verificar cual corresponde poner y agregarlo
    array = []
    i = 0
    while i < (len(M) + len(N)):
        if i == 0 and i < len(M) and i < len(N):
            if M[i] > N[i]:
                array.append(N[i])
            else:
                array.append(M[i])
        else:        
            if i < len(M):
                array.append(M[i])
            if i < len(N):
                array.append(N[i])
        i += 1
        
    return array


M = orderList(getList())
N = orderList(getList())

print()
print("M ordenando:",M)
print("N ordenado:",N)
print("Lista intercalada:", mix(M,N))


