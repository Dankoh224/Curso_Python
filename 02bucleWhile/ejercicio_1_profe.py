x = int(input("Introduce el valor: $"))
total = 0
while x != 0:
    if x > 0:
        total = x + total
        x = int(input("Introduce el siguiente valor: $"))
    else:
        print("Error, el monto es inválido")
        x = int(input("Introduce el valor del artículo: $"))
if total > 1000:
    total = total - total*10/100
    print("El total es : $" , total)
else:
    print("El total es : $" , total)
