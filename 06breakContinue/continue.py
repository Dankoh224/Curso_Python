# La sentencia continue, sirve para saltar una iteración en particular en el bucle en el que se encuentra la sentencia. Veamos un ejemplo:
palabra = "jirafa"
# Si quisieramos mostrar todas las letras, haríamos lo siguiente.
for i in palabra:
    print(i)
# Pero si quisieramos mostrar todas las letras a excepción de la r, haríamos esto:
print("Imprimir todas las letras de jirafa menos la 'r'.")
for i in palabra:
    if i == "r":
        continue
    print(i)
