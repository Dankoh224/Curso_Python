# Pasar de una lista bidimensional a dos listas unidimensionales y viceversa.
grupos = [
    [1,"A"],[2,"B"],[3,"C"],[4,"D"],[5,"E"],[6,"F"],[7,"G"],[8,"H"],[9,"I"],[10,"J"]
]
print(grupos)
print("La lista anidada anterior se separa en las siguientes listas:")
numeros = []
letras = []
for elemento in grupos:
    numeros.append(elemento[0])
    letras.append(elemento[1])
print(numeros)
print(letras)
grupoNuevo = []
for i in range(len(numeros)):
    grupoNuevo.append([numeros[i],letras[i]])
print("Luego, se vuelve a unir quedando:")
print(grupoNuevo)