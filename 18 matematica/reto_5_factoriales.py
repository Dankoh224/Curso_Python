import math

x=10

print(math.factorial(x))

def factorial(n):
    resultado = 1
    while n > 1:
        resultado = n*resultado
        n -= 1
    return resultado

print(factorial(10))

def factorial_2 (n):
    resultado = 1
    for i in range(1,n+1):
        resultado = resultado * i
    return resultado

print(factorial_2(10))

# Calcula el número de combinaciones sin repetición de n elementos tomados de n en n.
def combinaciones(n,k):
    f = 1
    for i in range(1,n+1):
        f = f * i
    g = 1
    for i in range(1,n-k+1):
        g = g * i
    h = 1
    for i in range(1,k+1):
        h = h * i
    resultado = f/(g*h)
    return resultado



def combinaciones_2(n,k):
    numerador = 1
    dif = n-k
    for i in range(n,dif,-1):
        numerador = numerador * i
    denominador = 1
    for i in range(1,k+1):
        denominador = denominador * i
    combinacion = numerador/denominador
    return combinacion

print(combinaciones_2(10000,3))
print(combinaciones(10000,3))
