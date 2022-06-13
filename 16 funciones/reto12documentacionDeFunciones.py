# Define una función que tome tres números y devuelva el que sea el intermedio de los tres. Si hay dos repetiodos, se devuelve el repetido. Si hay tres repetidos, se devuelve el único que hay.
def intermedio(a,b,c):
    lista = [a,b,c]
    lista.sort()
    return lista[1]

a = 8
b = 8
c = 8

print(intermedio(a,b,c))