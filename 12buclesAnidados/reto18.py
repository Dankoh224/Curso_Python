# Descifrar el mensaje "bdardmxmd py bkfsay pe ñaxa gy ugpra". Codificar un programa, que sabiendo la clave, descifre un mensaje cifrado. Luego, mediante un procedimiento de fuerza bruta, utilizar ese programa para tratar de descifrar este mensaje sin saber la clave.
abecedario = "abcdefghijklmnñopqrstuvwxyz"
mensaje = "bdardmxmd py bkfsay pe ñaxa gy ugpra"
for j in range (1,28):
    clave = j
    print(j,": ", end = "")
    for i in mensaje:
        if i == " ":
            print(" ", end = "")
        elif abecedario.index(i) < clave:
            posicion_anterior = 27 + abecedario.index(i) - clave
            print(abecedario[posicion_anterior], end = "")
        else:
            posicion_anterior = abecedario.index(i) - clave
            print(abecedario[posicion_anterior], end = "")
    print()