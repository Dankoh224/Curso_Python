# Definir una función en la que a un número (minuendo) se le reta otro (sustraendo), las veces que se indique (veces) -> 100-(5*3 veces) = 85.
def restasIndicadas (minuendo,sustraendo,veces):
    resultado = minuendo - sustraendo * veces
    return resultado

print(restasIndicadas(21,4,5))
