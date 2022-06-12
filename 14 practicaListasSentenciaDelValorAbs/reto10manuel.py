#Programa que muestra el reverso de una cadena de caracteres
cadena = "suena como latin"
reverso = ""
# for i in range(len(cadena)-1,-1,-1):
#     reverso = reverso+ cadena[i]
# print(reverso)

# for i in cadena:
#     reverso = i + reverso
# print(reverso)

reverso = cadena[::-1]
print(reverso)