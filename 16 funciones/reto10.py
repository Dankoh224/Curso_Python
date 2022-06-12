# Programa que permite convertir unidades de masa: kilogramos a libras y libras a kilogramos. 1 kg son 2.20462262 libras y 1 libra son 1/20462262
def kgAlb(kg):
    return kg * 2.20462262

def lbAkg(lb):
    return lb * 1/2.20462262

opcion = str(input("Ingrese 1 si desea convertir de kg a lb. Ingrese 2 si desea convertir de lb a kg"))
if opcion == "1":
    kg = int(input("Ingrese los kilogramos a convertir: "))
    print("La cantidad es equivalente a {} libras.".format(kgAlb(kg)))
elif opcion == "2":
    lb = int(input("Ingrese las libras a convertir: "))
    print("La cantidad es equivalente a {} kilogramos.".format(lbAkg(lb)))
else:
    print("La opción no es correcta.")
