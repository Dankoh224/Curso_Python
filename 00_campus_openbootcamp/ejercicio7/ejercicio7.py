# Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final. Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]
numero_inicio = 2
numero_final = 8
lista = []
for i in range(numero_inicio,numero_final):
    if numero_inicio % 2 != 0:
        lista.append(i)
    numero_inicio += 1       
print(lista)