# Cifrado César:
alfabeto = "abcdefghijklmnñopqrstuvwxyz"
mensaje = "danko hola"
clave = 7
for i in mensaje:
    posicion_i = mensaje.index(i)
    if i in alfabeto and 27 - clave > alfabeto.index(i):
        posicion_i_de_alfabeto = alfabeto.index(i)
        posicion_cifrado = posicion_i_de_alfabeto + clave
        cifrado = alfabeto[posicion_cifrado]
        print(cifrado, end = "")
    else:
        posicion_i_de_alfabeto = alfabeto.index(i)
        posicion_cifrado = posicion_i_de_alfabeto - 27 + clave
        cifrado = alfabeto[posicion_cifrado]
        print(cifrado, end = "")