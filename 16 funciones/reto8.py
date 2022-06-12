# Define una funciòn que indique si un nùmero es par o impar:
def par(numero):
    if numero % 2 == 0:
        return True
    return False
numero = 543
if par(numero):
    print("Es par")
else:
    print("Es impar")
print(par(numero))