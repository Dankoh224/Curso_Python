# Mostrar todos los números capicúas entre 10.000 y 12.000.
inicio = 10000
final = 12000

for i in range (inicio,final):
    num = str(i)
    reverso = num[::-1]
    if num == reverso:
        print("El número {} ES capicúa.".format(num))


num = str(input("Ingrese un número: "))
reverso = num[::-1]
print(reverso)