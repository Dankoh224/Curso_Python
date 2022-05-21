x = int(input("Ingresa un número: "))
y = int(input("Ingresa un número: "))
z = int(input("Ingresa un número: "))

if x>y and x>z:
    print("El número ",x," es el mayor.")

elif y>x and y>z:
    print("El número ",y," es el mayor.")

else:
    print("El número ",z," es el mayor.")

