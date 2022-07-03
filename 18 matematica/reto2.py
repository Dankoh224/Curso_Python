# define una función que realice una potencia si ** y sin math:
def potencia (base, exponente):
    resultado = 1
    for i in range(exponente):
        resultado = resultado * base
    return resultado

print(potencia(-4,3))