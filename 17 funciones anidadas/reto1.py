# funcion que devuelve el mayor de tres valores
a = 1
b = 2
c = 3
def mayor_de_2(a,b):
    if a > b:
        return a
    else:
        return b



def mayor_de_tres(a,b,c):
    mayor = mayor_de_2(a,b)
    if mayor > c:
        return mayor
    else:
        return c

print(mayor_de_tres(4,5,6))