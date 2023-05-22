# Ingresa nombre y apellido e imprimelo al reves.
nombre = 'Danko'
apellido = 'Valderrama'

for i in apellido:
    alreve = len(apellido) - apellido.index(i) -1
    print(apellido[alreve], end = ' ')

for i in nombre:
    alreve = len(nombre) - nombre.index(i) -1
    print(nombre[alreve], end = ' ')