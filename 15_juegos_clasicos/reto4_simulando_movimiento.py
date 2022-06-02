# Crear un programa que simule el movimiento de un dibujo usando bucles.
import os
import time
contador = 0
movimiento = ""
while contador < 15:
    time.sleep(0.2)
    os.system("cls")
    print("{}   O  ".format(movimiento))
    print("{}  /|\ ".format(movimiento))
    print("{}  / | ".format(movimiento))
    time.sleep(0.2)
    os.system("cls")
    print("{}    O  ".format(movimiento))
    print("{}   (|\ ".format(movimiento))
    print("{}   | | ".format(movimiento))
    time.sleep(0.2)
    os.system("cls")
    print("{}     O  ".format(movimiento))
    print("{}    /|\ ".format(movimiento))
    print("{}    | \ ".format(movimiento))
    time.sleep(0.2)
    os.system("cls")
    print("{}      O  ".format(movimiento))
    print("{}     /|) ".format(movimiento))
    print("{}     | | ".format(movimiento))
    movimiento += "    "
    contador += 1