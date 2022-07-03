# Realiza una función que saque raíz cuadrada.
# raiz de 4 y raiz de 9 la diferencia entre ellos es:
def raiz(numero):
    x = 0.000001
    while True:
        resultado = x * x
        if resultado >= numero:
            return x
        else:
            x = x + 0.000001

print(raiz(4))
