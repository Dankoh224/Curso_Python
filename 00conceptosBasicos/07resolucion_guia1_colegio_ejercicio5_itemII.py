nota1 = float(input("Ingresa la 1ra nota: "))
nota2 = float(input("Ingresa la 2da nota: "))
nota3 = float(input("Ingresa la 3ra nota: "))
nota4 = float(input("Ingresa la 4ta nota: "))
nota5 = float(input("Ingresa la 5ta nota: "))

promedio = (nota1+nota2+nota3+nota4+nota5)/5

if promedio >= 40:
    print("Felicitaciones, pasaste de curso con un ", promedio, ". Felicidades.")

else:
    print("Lo sentimos. No pasaste de curso. Tienes un promedio de ", promedio, ".")
