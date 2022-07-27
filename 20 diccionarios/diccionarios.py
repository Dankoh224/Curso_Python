# # Un dicionario es otro tipo de forma de guardar datos. Tenemos las listas, las tuplas y los diccionarios. El diccionario se compone de elementos que a su vez se deviden en clave e información que asociar a esa clave. Veamos el siguiente ejemplo de diccionario de telefonos.
# telefonos = {
#     "jose": 1234,
#     "maría": 2142,
#     "andrés": 3242,
#     "lucía": 3432
# }

# # Consultar un valor asociado a una clave :
# print(telefonos["maría"])

# # Agregar un elemento:
# telefonos["jorge"] = 4543
# print(telefonos["jorge"])

# # Modificar elementos:
# telefonos["jorge"] = 4732
# print(telefonos["jorge"])

# # Eliminar elementos:
# del telefonos["jorge"]
# print(telefonos)

# # Eliminar todo el diccionario:
# del telefonos


# RECORRER ELEMENTOS CON BUCLE FOR:
# Diccionario de mascotas:
d = {"animal": "perro","color":"blanco","edad":4}

# Si queremos imprimir las CLAVES del diccionario usamos el siguiente bucle:
for clave in d:
    print(clave)
# Sin embargo, también es posible usar el método VALUES:
print(d.keys())

# Si queremos imprimir los VALORES del diccionario usamos el siguiente bucle:
for clave in d:
    print(d[clave])
# Sin embargo, también es posible usar el método KEYS:
print(d.values())

# Si queremos imprimir los pares de CLAVES y VALORES del diccionario usamos el siguiente bucle:
for clave in d:
    print("{}: {}.".format(clave,d[clave]))
# Sin embargo, también es posible usar el método ITEMS:
print(d.items())

# IMPORTANTE: los métodos enseñados no devuelven listas, pero si pueden transformarse en listas. Ejemplo:
print(list(d.items()))

# También existen otras formas de recorrer elementos usando bucles, por ejemplo:
for elemento in d.items():
    print(elemento)
# De esta forma se imprimirán los pares en forma de tuplas, sin embargo, si quisieramos imprimir estos elementos en una forma más formateada, haremos lo siguiente:
for elemento in d.items():
    print(elemento[0],elemento[1])
# Sin embargo esto no se suele realizar, ya que existe una forma mejor de llevarlo a cabo:
for clave, valor in d.items():
    print(clave,valor)