# Crear un programa que simule el movimiento de un dibujo usando bucles.
import os
import time
contador = 0
movimiento = ""
movimiento_pasto = ""
while contador < 50:
    os.system("cls")
    print("{0}       wwwww                                     ___________                     {0}".format(movimiento))
    print("{0}      c(°^°)>                                                                    {0}".format(movimiento))
    print("{0}      ___|                                            _______                    {0}".format(movimiento))
    print("{0}     /   |\  /                                                           ______  {0}".format(movimiento))
    print("{0} _   \   | \/                                   _                _               {0}".format(movimiento))
    print("{0}  \     /  \     ___                                                             {0}".format(movimiento))
    print("{0}    \ /      \                                                                   {0}".format(movimiento))
    print("{0}_______________\_________________________________________________________________{0}".format(movimiento_pasto))
    print("           MMM         MMMMMMM                          MMM         MMMMMMM                  ")
    print("                   MMMMMMMMMM                   MMMMMMMMMM                 MMM             M ")
    time.sleep(0.1)
    os.system("cls")
    movimiento += " "
    movimiento_pasto += "_"
    contador += 1