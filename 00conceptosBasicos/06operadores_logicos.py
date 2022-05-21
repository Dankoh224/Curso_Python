print("Conjunción (and): ")

num = int(input("Escribe un número mayor a 2 y menor a 5: "))

if num > 2 and num < 5:
    print("El número cumple la condición. Fin del programa.")
else:
    print("El número no cumple con la condición. Fin del programa.")

print("Disyunción (or): ")

num = int(input("Escribe un número mayor a 6 o menor a 1: "))

if num > 6 or num < 1:
    print("El número cumple la condición. Fin del programa.")
else:
    print("El número no cumple con la condición. Fin del programa.")


print("Negación (not): ")

num = int(input("Escribe un número igual a 5: "))

if not num == 5:
    print("El número no cumple la condición. Fin del programa.")
else:
    print("El número cumple con la condición. Fin del programa.")
