# Programa que convierte temperaturas: Farenheit a celcius y celcius a farenheint. °F = (°C*1.8)+32. C° = (°F-32)/1.8
def fAc(fa):
    return (fa - 32) / 1.8

def cAf(ce):
    return ce * 1.8 + 32

opcion = str(input("Ingrese 1 si desea convertir de °F a °C. Ingrese 2 si desea convertir de °C a °F: "))
if opcion == "1":
    fa = int(input("Ingrese los °F a convertir: "))
    print("La cantidad es equivalente a {} °C.".format(fAc(fa)))
elif opcion == "2":
    ce = int(input("Ingrese los °C a convertir: "))
    print("La cantidad es equivalente a {} °F.".format(cAf(ce)))
else:
    print("La opción no es correcta.")
