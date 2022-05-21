#Programa que te pide que adivines un número del 1 al 10 y te pida números constantemente hasta que lo adivines. Añade un contador que te diga los intentos que has necesitado.
x = int(input("Adivina el número, está entre 1 y 10: "))
intento = 0
while x != 6:
    print("No es {}, intenta de nuevo.".format(x))
    x = int(input("Adivina el número, está entre 1 y 10: "))
    intento = intento + 1
else:
    print("¡Bien! ¡Adivinaste! El número es el {}.".format(x))
