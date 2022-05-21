# Encontrar la palabra más larga y si hay varias con igual longitud la primera de todas .
lista = ["mesa","armario","silla","lampara","cuadro"]
largoPalabra = 0
palabra = ""
mayor = 0
for i in lista:
    largoPalabra = len(i)
    if largoPalabra > mayor:
        mayor = largoPalabra
for i in lista:
    if len(i) == mayor:
        palabra = i
        break
print("La palabra más larga es {} con {} letras.".format(palabra,mayor))