#Programa que muestra el reverso de una cadena de caracteres
cadena = "suena como latin"
reverso = list(cadena)
reverso.reverse()
cadenaReverso = ""
for i in reverso:
    cadenaReverso = cadenaReverso + i
print(cadenaReverso)