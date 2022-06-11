# Programa que te pide que introduzcas productos y crea una lista de la compra con esos productos que te muestra al final.
compras = []
continuar = True
while continuar:
    producto = str(input("Ingrese producto: "))
    compras.append(producto)
    continuar = str(input("¿Deseas ingresar otro producto? S/N: "))
    continuar = continuar.lower()
    if continuar == "n":
        continuar = False
print(compras)