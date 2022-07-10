# Conjuntos: son grupos de elementos UNICOS y DESORDENADOS.
# Cómo son únicos, no importa si están en orden o desorden.

conjunto = set() # Esto se hace para inicializar un conjunto vacío.

# PYTHON diferencia diccionarios de conjuntos solo gracias al SET().

# Por otra parte, si quiero crear inmediatamente un conjunto con sus elementos, no es necesario usar set, ya que python nota que es un conjunto al no hallar puntos y comas dentro del arreglo

conjunto = {1,2,3,"Hola",4.332,12,3,4,5,5,"Hola","a"}

# AGREGAR un valor al conjunto:
conjunto.add(77)

# ELIMINAR un elemento:
conjunto.discard("Hola")

# ELIMINAR TODOS los elementos:
conjunto.clear()

conjunto.add(3)

# BUSCAR un elemento (puede escribirse un "in" o un "not in"):
x = 3 in conjunto

# AGREGAR MUCHOS datos:
conjunto.update([1,2,3,4,5,6,7])

# UNION de dos o más conjuntos:
conjunto1 = {1,4,6,3,8,"dan"}
conjunto2 = {"perro",3,6,4,1,"gato",7}
union = conjunto1 | conjunto2

# INTERSECCIÓN de dos o más conjuntos:
interseccion = conjunto1 & conjunto2

# DIFERENCIA entre dos conjuntos:
diferencia = conjunto2 - conjunto1

# DIFERENCIA SIMÉTRICA entre dos conjuntos: Retorna un conjunto nuevo que contiene elementos que están incluidos en el conjunto1 o en conjunto2, pero no en los dos a la vez).
diferenciaSimetrica = conjunto1 ^ conjunto2


# CANTIDAD de elementos:
largo = len(conjunto2)

# BUCLE FOR:
for i in conjunto2:
    x = 8

# SUBCONJUNTO retorna True o False si el conjunto1 está contenido en el conjunto2:
x = conjunto1.issubset(conjunto2)


# Elimina y retorna un elemento cualquiera del conjunto. Lanza la excepción KeyError si el conjunto estaba vacío.
x = conjunto1.pop()


# Conjuntos DISCONEXOS (si no tienen elementos en común):
conjunto1 = {3,4,5}
conjunto2 = {6,7,8}
x = conjunto1.isdisjoint(conjunto2)

# Conjuntos INMUTABLES:
conjunto1 = frozenset({1,2,3})
