# Tenemos una lista de temperaturas. Hay que comprobar que todas las temperaturas están entre 18 y 25 incluidos. Si alguno no cumple la condición se cumple el programa y lo indica, si no va mostrando que la temperatura verificada es correcta.
temperaturas = [19,22,21,24,23,27,21,20,19,18,21,20]
for i in temperaturas:
    if 18 <= i <= 25:
        print("La temperatura verificada es correcta.")
    else:
        print("El programa ha finalizado.")
        break