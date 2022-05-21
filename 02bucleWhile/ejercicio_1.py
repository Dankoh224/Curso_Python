x = int(input("Ingresa el valor del articulo"))
suma = 0

while x != 0:

    while x > 0:
        suma = suma + x
        print("El subtotal es: ", suma)
        x = int(input("Ingresa el valor del siguiente articulo"))
    
    while x < 0:
        print("El valor debe ser positivo.")
        x = int(input("Ingresa el valor del articulo"))


if suma > 1000:
    print("El total es ", suma - suma * 10/100 )

else:
    print("El total es ", suma)
