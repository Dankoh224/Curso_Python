# Define una función anidada que tome tres números y devuelva el que sea el intermedio de los tres. Si hay dos repetidos, se devuelve el repetido. Si hay tres repetidos, se devuelve el único que hay.
def mayor_de_dos(a,b):
    if a > b:
        return a
    else:
        return b

def intermedio(a,b,c):
    mayor1 = mayor_de_dos(a,b)
    mayor2 = mayor_de_dos(a,c)
    if mayor1 > mayor2:
        return mayor2
    elif mayor1 < mayor2:
        return mayor1
    else:
        return mayor_de_dos(b,c)
print(intermedio(1,2,3))
print(intermedio(1,3,2))
print(intermedio(2,1,3))
print(intermedio(2,3,1))
print(intermedio(3,1,2))
print(intermedio(3,2,1))
print(intermedio(1,2,2))
print(intermedio(2,1,2))
print(intermedio(2,2,1))
print(intermedio(2,2,3))
print(intermedio(3,2,2))
print(intermedio(2,3,2))
print(intermedio(2,2,2))

