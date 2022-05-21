# Función INT: cambia un elemento tipo string a entero:
numero = "2"
numero = int(numero)
print(type(numero))
# También cambia un número flotante a entero:
numero = 3.5
numero = int(numero)
print(numero)
print(type(numero))
# Función FLOAT: cambia un elemento tipo string o int a float:
numero = 5
numero = float(numero)
print(numero)
print(type(numero))
numero = "3"
numero = float(numero)
print(numero)
print(type(numero))

# Función TUPLE: crea una tupla con los elementos que le pasamos como argumentos. IMPORTANTE: el argumento debe ser un iterable. Ejemplo:
tupla = tuple([1,2,3])
print(tupla)
tupla = tuple((3,2,4))
print(tupla)
tupla = tuple(range(10))
print(tupla)

# Función LIST: crea una lista con los elementos que le pasamos como argumentos. IMPORTANTE: el argumento debe ser un iterable. Ejemplo:
numero = list((1,2,3))
print(numero)
numero = list(range(1,11))
print(numero)