# Un dicionario es otro tipo de forma de guardar datos. Tenemos las listas, las tuplas y los diccionarios. El diccionario se compone de elementos que a su vez se deviden en clave e información que asociar a esa clave. Veamos el siguiente ejemplo de diccionario de telefonos.
telefonos = {
    "jose": 1234,
    "maría": 2142,
    "andrés": 3242,
    "lucía": 3432
}

# Consultar un valor asociado a una clave :
print(telefonos["maría"])

# Agregar un elemento:
telefonos["jorge"] = 4543
print(telefonos["jorge"])

# Modificar elementos:
telefonos["jorge"] = 4732
print(telefonos["jorge"])

# Eliminar elementos:
del telefonos["jorge"]
print(telefonos)

# Eliminar todo el diccionario:
del telefonos 
print(telefonos)