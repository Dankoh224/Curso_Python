# Escribe una función que pueda decirte si un número (número entero) es primo o no.
def numero_primo(num):
    for i in range(2,num):
        if num % i == 0:
            a = ("El número {} NO es un número primo.".format(num))
            break
        if i + 1 == num:
            a = ("El número {} es un número primo.".format(num))
    return a

print(numero_primo(32))