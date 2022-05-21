# Para crear dos variables al mismo tiempo:
"""x,y = 2,3
print(x)
print(y)"""

# Pero si hay distinta cantidad de variables y datos se generará un error.
x,y,z = 1,2,3
# Para que esto no suceda, tienes que tener la misma cantidad de variables y datos a ambos lados. A no ser que utilices el operador de desempaquetado.
x,y,*z = 1,2,3,4
print(x)
print(y)
print(z)
# IMPORTANTE: a la variable z, el programa le ha asignado la lista [3,4].

# También se puede tomar una lista, por ejemplo:
numeros = [1,2,3,4,5,6,7,8,9]
x,y,*z = numeros
print(x)
print(y)
print(z)
# IMPORTANTE: a la variable z, el programa le ha asignado la lista [3,4,5,6,7,8,9]. Por lo tanto, siempre a la variable que tiene el operador de desempaquetado, obtendrá el resto de los datos faltantes. Ejemplo:
numeros = [1,2,3,4,5,6,7,8,9]
x,*y,z = numeros
print(x)
print(y)
print(z)

# Ejemplo:
letras = ["a","b","c","d","e","f"]
primera, segunda, *resto, ultima = letras
print(primera)
print(segunda)
print(resto)
print(ultima)
