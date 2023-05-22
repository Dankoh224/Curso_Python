# Definir una función que tome tres números como argumentos y devuelva el mayor.
def max_de_tres(a,b,c):
    if a>b>c:
        return a
    elif a>c>b:
        return a
    elif b>c:
        return b
    elif c>b:
        return c
    else:
        return 'los números son iguales'

print(max_de_tres(1,1,1))