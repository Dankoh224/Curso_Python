eleccion = None
while eleccion is None or eleccion > 5:
    eleccion = int(input("Escribe un numero mayor a 5: "))
    print("La variable es mayor que 5.")
else:
    print("La variable es menor o igual que 5.")