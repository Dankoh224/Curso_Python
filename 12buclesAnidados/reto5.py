# Programa que muestra todas las posibles combinaciones para poder abrir un candado de clave de tres ruedas.
for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            for h in range(10):
                print(i,j,k,h)