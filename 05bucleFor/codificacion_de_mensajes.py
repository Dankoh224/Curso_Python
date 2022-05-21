for i in range(5):
    mensaje = input("Ingresa el mensaje secreto: ")
    cifras = int(input("Cuantas veces vas a mover: "))
    abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in mensaje:
        if i == " ":
            print(end = " ")
        elif i == ",":
            print(end = ",")
        elif i == ".":
            print(end = ".")
        elif i == "?":
            print(end = "?")
        elif i == "¿":
            print(end = "¿")
        elif i == "!":
            print(end = "!")
        elif i == "¡":
            print(end = "!")
        else:
            indice = abecedario.index(i)
            letra_cifrada = (indice + cifras)%27
            print(abecedario[letra_cifrada], end = "")
    print(" ")

