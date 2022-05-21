# Generar una tupla a raíz de un elemento iterable (como una lista)
from re import S


t = tuple([1,2,3])
print(t)
# Generar una tupla a partir de un elemento tipo range.
t = tuple(range(10))
print(t)
# Generar una lista a raíz de un elemento iterable (como una tupla)
l = list((1,2,3))
print(l)
# Generar una lista a partir de un elemento tipo range.
l = list(range(10))
print(t)
# Crear tupla o lista vacía.
t = ()
l = []
print(t)
print(l)
t = tuple()
l = list()
print(t)
print(l)
# En el caso de las listas, esta última función nos servirá para realizar copias del objeto, con distintos ID. IMPORTANTE: las listas son objetos mutables y las tuplas inmutables, por lo tanto, al cambiar la tupla original, se verá afectada su copia.
s = (1,2,3)
v = s
print(s)
print(v)
print(id(s))
print(id(v))



# Observar que ambos ID son identicos, eso significa que la variable s y la variable v apuntan al mismo objeto. Sin embargo, si hacemos lo mismo con las listas, las variables no apuntaran al mismo objeto, ya que se hará una copia con distinto ID:
m = [1,2,3,4]
n = m
print(id(m))
print(id(n))
m.append(5)
print(m)
print(n)
# Así nos quedamos con la misma lista. Para poder copiar y tener una lista completamente nueva, haremos lo siguiente:
m = [1,2,3,4]
print(m)
n = list(m)
print(n)
print(id(m))
print(id(n))
# Ahora si le agrego un elemento a la lista m, no afectará a la lista n.
m.append(5)
print(m)
print(n)



