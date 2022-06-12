cadena = "El sol sale por el este. Se pone por el oeste"
split = cadena.split()
print(split)
# Si no se le asigna nada, crea una lista de elementos con las palabras de la cadena. Los espacios hacen esta separación.
# Si se le pone un punto, hace la separación con los puntos.
split = cadena.split(".")
print(split)
# Y si se le pone una letra, hace la separación con esa letra.
split = cadena.split("o")
print(split)

# Ahora, si con el método split separabamos una cadena en una lista, con el método join podemos formar una cadena con los elementos de una lista.
cadenaNueva = " ".join(split)
print(cadenaNueva)
# Al método join se le puede agregar lo que se quiera dentro del espacio.

# El método .replace() reemplaza un carácter por otro. Ejemplo:
cadenaNueva = cadenaNueva.replace(".","!")
print(cadenaNueva)
# Al método replace se le puede agregar un 3er argumento, donde usando números, le pediremos hasta cuantas veces haremos tal cambio.

# Por último, el método isalpha() alfabetico y isalnum(), alfanumerico, nos diran si es verdadero o falso, si una cadena es de ese tipo.
cadena = "casa"
cadena2 = "123"
cadena3 = "123."
perro = "cadena".isalpha()
print(perro)
gato = "cadena2".isalpha()
print(gato)
dedo = "cadena2".isalnum()
print(dedo)
cubo = "cadena3".isalnum()
print(cubo)