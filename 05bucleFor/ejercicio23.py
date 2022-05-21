"""Realizar un programa que pregunte al usuario una cantidad a invertir en soles, el interés 
anual y el número de años, finalmente muestre le capital obtenido  en la inversión durante el
periodo anual establecido."""
soles = int(input("Ingrese soles a invertir: "))
interesAnual = float(input("Ingrese interés anual: "))
cantidadAnos = int(input("Ingrese la cantidad de años de inversión: "))
for i in range(cantidadAnos):
    soles = soles + (soles*interesAnual/100)
print(soles)