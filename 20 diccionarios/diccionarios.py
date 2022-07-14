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


# # RECORRER BUCLE FOR:
# # lista nueva:
d = {"animal": "perro","color":"blanco","edad":4}
# print(d.keys())

# # Recorrer las claves del diccionario
# for k in d:
#     print(k)


# # Recorrer los valores del diccionario
for k in d:
    print(d[k])

# Recorrer los valores del diccionario
# for v in d.values():
#     print(v)

# # Recorrer los pares clave valor
# for i in d.items():
#     print(i)