# Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
def max(a,b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return 'los números son iguales'

print(max(-3,12))