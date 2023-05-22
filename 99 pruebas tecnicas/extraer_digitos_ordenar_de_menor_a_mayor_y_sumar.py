# Realiza un programa:
# 1. Que extraiga los digitos de la siguiente cadena de texto.
# 2. Que los ordene de menor a mayor y los devuelva en una cadena de texto.
# 3. Que sume todos los digitos y devuelva el resultado de la suma total.
# Todos los resultados deben ser mostrados por consola de manera simultanea.

text = '41n2jjg3g5smdksfuu6'
lista_numeros = []
for i in text:
    if i in '1234567890':
        numero = int(i)
        lista_numeros.append(numero)

lista_numeros.sort()
print(lista_numeros)
print(sum(lista_numeros))

    
