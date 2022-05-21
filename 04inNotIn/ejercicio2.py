# Programa que dice la cantidad de vocales y consonantes que tiene una palabra que introduzca el usuario.
a = "danko"
print(a)
vocales = "aeiou"
consonantes = "bcdfghjklmnñpqrstvwxyz"
totalVocales = 0
totalConsonantes = 0
n = 0
while n <= len(a) - 1:
    if a[n] in vocales:
        totalVocales += 1
    elif a[n] in consonantes:
        totalConsonantes += 1
    n += 1
print("La cantidad de vocales es {} y la cantidad de consonantes es {}.".format(totalVocales,totalConsonantes))
