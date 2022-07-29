# Programa que guarda un registro de todas las búsquedas que se realizan en un diccionario, tanto de los elementos que están, como de los que no están.
prefijos_internacionales = {
    "COLOMBIA": 57,
    "ARGENTINA": 54,
    "PERU": 51,
    "MEXICO": 52,
    "BOLIVIA": 591,
    "CHILE": 56,
    "ESPAÑA": 34,
    "ECUADOR": 593
}
conteo_paises = {}
print("------------------------")
print("PREFIJOS INTERNACIONALES")
print("------------------------")

while True:

    pais = str(input("País ('q' para salir): ").upper())
    if pais == "Q":
        print("Programa finalizado")
        break

    prefijo = prefijos_internacionales.setdefault(pais,"no disponible.")
    
    print("{}: {}".format(pais,prefijo))

    conteo_paises.setdefault(pais,0)
    conteo_paises[pais] += 1

    print("------------------------")
    print("REGISTRO DE CONSULTAS")
    for llave, valor in conteo_paises.items():
        print("{}: {}".format(llave,valor))
    print("------------------------")






