# Haz un programa en el que se compruebe si un número es múltiplo de otro, mediante una función con dos return.
def multiplos(num1,num2):
    if num1 % num2 == 0:
        return True
    return False

num1 = 45
num2 = 10

if multiplos(num1,num2):
    print("El número 1 es múltiplo del número 2.")
else:
    print("El número 1 NO es múltiplo del número 2.")

