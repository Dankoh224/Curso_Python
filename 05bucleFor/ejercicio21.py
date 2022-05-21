#ejercicio 21: Escribir una oración y mostrar en pantalla las vocales que aparecen (sin repetir las vocales).
oracion = str(input("Ingrese la oración: "))
oracion = list(oracion)
print(oracion)
for i in oracion:
    x = oracion.count(i)
    if x != 1:
        oracion.remove(i)
    else:
        print(i)
