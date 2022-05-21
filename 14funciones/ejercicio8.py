# Haz un programa en el que se compruebe si un número es múltiplo
# de otro, mediante una función con dos return.
def multiploDeUnNumero (multiplo,numero):
    if multiplo % numero == 0:
        return True
    else:
        return False
numero = int(input("Ingrese un número: "))
multiplo = int(input('Ingrese el "múltiplo" de ese número: '))

print(multiploDeUnNumero(multiplo,numero))