# Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
edad = int(input("Ingrese su edad: "))
if edad >= 18 and edad < 110:
    print("Usted es mayor de edad.")
elif edad >= 0 and edad < 18:
    print("Usted es menor de edad.")
else:
    print("La edad ingresada es incorrecta.")