# En la varible text dispones de una cadena de texto
# Debes contar las palabras y devolver cuántas veces se repiten cada una de ellas.
# Ej. Nadie aparece 2 veces.
text = 'Creo que a veces es la gente de la que nadie espera nada, la que hace cosas que nadie puede imaginar.'

# Primero creamos una lista con todas las palabras de text.

lista_palabras = []
palabra = ""

for i in text:
    if (i == " ") or (i == ",") or (i == "."):
        if len(palabra) > 0:
            lista_palabras.append(palabra)
        palabra = ""
    else:
        palabra += i

# Finalmente contamos la cantidad de veces que se repiten las palabras, imprimimos y borramos.

bandera = True
while bandera:
    for i in lista_palabras:
        repeticiones = lista_palabras.count(i)
        print('La palabra "{}" se repite: {} veces.'.format(i,repeticiones))

        while repeticiones > 0:
            lista_palabras.remove(i)
            repeticiones = lista_palabras.count(i)
        break
    if len(lista_palabras) == 0:
        bandera = False
