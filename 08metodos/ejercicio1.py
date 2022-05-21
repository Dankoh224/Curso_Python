# Programa que recoge todas las palabras de un texto y las devuelve sin espacios, comas, ni puntos.
cadena = "Estaba allí. Era un pájaro, en la ventana. pero entonces, de repente, se echó a volar."
cadena = cadena.split()
print(cadena)
for i in cadena:
    i = i.strip(".")
    i = i.strip(",")
    print(i, end = "")