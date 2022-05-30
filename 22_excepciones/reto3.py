# Programa que calcula las raíces cuadradas:
import math
try:
    numero = float(input("Ingrese número: "))
    raiz = math.sqrt(numero)
    print(raiz)
except:
    print("No se pueden calcular las raíces de un número negativo")
