#ejercicio 21: Escribir una oración y mostrar en pantalla las vocales que aparecen (sin repetir
#las vocales).
oracion = str(input("Ingrese oración: "))
for i in "aeiou":
    if i in oracion:
        print(i)
        

