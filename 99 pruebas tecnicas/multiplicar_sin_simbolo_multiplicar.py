# Haz una función multiplicar que no utilice el símbolo de multiplicación.
def multiplica_sin_simbolo(a,b):
    resultado = 0
    while a > 0:
        resultado += b
        a -= 1
    return resultado
print(multiplica_sin_simbolo(-12,-12))


