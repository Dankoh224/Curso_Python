# Programa que guarda un registro de todas las búsquedas que se realizan en un diccionario, tanto de los elementos que están, como de los que no están.
prefijos = {
    "COLOMBIA": 57,
    "ARGENTINA": 54,
    "PERU": 51,
    "MEXICO": 52,
    "BOLIVIA": 591,
    "CHILE": 56,
    "ESPAÑA": 34,
    "ECUADOR": 593
}
bandera = True
while bandera:
    print("PREFIJOS INTERNACIONALES")
    print("------------------------")
    pais = input("País ('q' para salir): ").upper()

    print(prefijos.get(pais,"No disponible."))

    for clave, prefijo in prefijos.items():
        if pais == clave:
            print("{}: {}".format(pais, prefijo))

    if pais == "q":
        print("Gracias por haber usado el programa.")
        break

    else:
        print("------------------------")
        print("Registro de búsquedas:")
        prefijos.setdefault(pais,0)
        prefijos[pais] += 1
        for clave, prefijo in prefijos.items():
            if pais == clave:
                print("{}: {}".format(pais, prefijo))
        print("------------------------")

    