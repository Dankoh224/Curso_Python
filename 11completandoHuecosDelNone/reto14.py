#Encontrar la palabra más larga y si hay varias con igual longitud, la primera de todas.
listaPalabras = ["mesa","armario","silla","lámpara","cuadro"]
mayor = 0
for i in range(len(listaPalabras)):
    if len(listaPalabras[i]) > mayor:
        mayor = len(listaPalabras[i])
        palabraMayor = listaPalabras[i]
print(palabraMayor)