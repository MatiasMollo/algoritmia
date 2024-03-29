'''
Una editorial determina el precio del libro en base a las páginas que tiene
Costo básico: $5000
Agregado por página en encuadernación rústica: $32
Si supera las 300 páginas la encuadernación es de tela y suma $1200
Si supera las 600 páginas se incrementa el costo en otros $3360
Calcular el costo en base al numero de páginas
'''

paginas = float(input("Ingrese el número de páginas: "))

valor = 5000 + paginas*32

'''
Aclaración: Si el libro supera las 600 páginas se cuenta tambien el importe de las 300
ya que el enunciado dice que al superar las 600 el costo se incrementa en "OTROS" 3360
'''
if(paginas >= 300):
    valor += 1200
if(paginas >= 600):
    valor += 3360

print("Valor del libro: $%d" % valor)
