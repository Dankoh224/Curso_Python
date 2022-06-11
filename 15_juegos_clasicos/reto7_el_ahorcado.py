# 1. Elegir aleatoriamente una palabra de una lista de palabras. 
# 2. Mostrar el dibujo de una horca.
# 3. Mostrar un guión bajo por cada letra de la palabra.
# 4. Pedir al usuario que introduzca una letra:
#       Si no es una única letra indicarlo. Si ya se ha dicho indicarlo.
# 5. Comprobar si esa letra está contenida en la palabra elegida.
# 6. Si está: Volver a mostrar el dibujo de la horca como la última vez.
#       Sustituir el guión correspodiente por la letra dicha.
# 7. Si no está: Mostrar el dibujo de la horca al que se añade una parte.
#       Volver a mostrar los guiones como la última vez.
# 8. Si se falla 6 veces: Se completa el dibujo del ahorcado.
# Se muestra que se ha perdido.
# 9. Si se aciertan todas las letras de la palabra: Se muestra que se ha ganado.
import random
import os
contador = 0
# Paso 1: Obtener una palabra a adivinar.
listaPalabras = ["perro","escalera","hipopotamo","cordillera"]
palabraAdivinar = listaPalabras[random.randint(0,len(listaPalabras))]
print(palabraAdivinar)

print("*************************")
print("*** JUEGO EL AHORCADO ***")
print("*************************")
print("             !===N       ")
print("                 N       ")
print("                 N       ")
print("                 N       ")
print("           =======       ")
print()

# Paso 3: Mostrar un guión bajo por cada letra de la palabra.
for i in palabraAdivinar:
    print("_", end = " ")
print()

# Paso 4: Pedir al usuario que introduzca una letra. Si no es una única letra indicarlo. Si ya se ha dicho indicarlo.
bandera = True
while bandera:
    letra = str(input("Ingrese una letra: "))
    if len(letra) != 1:
        print("Ingrese solo una letra.")
    elif letra in "0123456789":
        print("No puede ingresar números.")
    else:
        bandera = False

# 5. Comprobar si esa letra está contenida en la palabra elegida.
# 6. Si está: Volver a mostrar el dibujo de la horca como la última vez. Sustituir el guión correspodiente por la letra dicha.
# 7. Si no está: Mostrar el dibujo de la horca al que se añade una parte. Volver a mostrar los guiones como la última vez.

guiones = []
if letra in palabraAdivinar:
    print("Adivinaste, la letra que ingresaste es parte de la palabra a adivinar.")
    print()
    print("*************************")
    print("*** JUEGO EL AHORCADO ***")
    print("*************************")
    print("             !===N       ")
    print("                 N       ")
    print("                 N       ")
    print("                 N       ")
    print("           =======       ")
    print()

# En estas líneas guardaremos las letras en una lista e imprimiremos.

    for i in palabraAdivinar:
        if letra == i:
            guiones.append("{} ".format(i))
        else:
            guiones.append("_ ")
    for i in guiones:
        print(i,end=" ")
    print()

if letra not in palabraAdivinar:
    contador += 1
    if contador == 1:
        print("La letra escogida no pertenece a la palabra a adivinar.")
        print()
        print("*************************")
        print("*** JUEGO EL AHORCADO ***")
        print("*************************")
        print("             !===N       ")
        print("             o   N       ")
        print("                 N       ")
        print("                 N       ")
        print("           =======       ")
        print()
    elif contador == 2:
        print("La letra escogida no pertenece a la palabra a adivinar.")
        print()
        print("*************************")
        print("*** JUEGO EL AHORCADO ***")
        print("*************************")
        print("             !===N       ")
        print("            _o   N       ")
        print("                 N       ")
        print("                 N       ")
        print("           =======       ")
        print()
    elif contador == 3:
        print("La letra escogida no pertenece a la palabra a adivinar.")
        print()
        print("*************************")
        print("*** JUEGO EL AHORCADO ***")
        print("*************************")
        print("             !===N       ")
        print("            _o_  N       ")
        print("                 N       ")
        print("                 N       ")
        print("           =======       ")
        print()
    elif contador == 4:
        print("La letra escogida no pertenece a la palabra a adivinar.")
        print()
        print("*************************")
        print("*** JUEGO EL AHORCADO ***")
        print("*************************")
        print("             !===N       ")
        print("            _o_  N       ")
        print("             |   N       ")
        print("                 N       ")
        print("           =======       ")
        print()
    elif contador == 5:
        print("La letra escogida no pertenece a la palabra a adivinar.")
        print()
        print("*************************")
        print("*** JUEGO EL AHORCADO ***")
        print("*************************")
        print("             !===N       ")
        print("            _o_  N       ")
        print("             |   N       ")
        print("            /    N       ")
        print("           =======       ")
        print()
    elif contador == 6:
        print("La letra escogida no pertenece a la palabra a adivinar.")
        print()
        print("*************************")
        print("*** JUEGO EL AHORCADO ***")
        print("*************************")
        print("             !===N       ")
        print("            _o_  N       ")
        print("             |   N       ")
        print("            / \  N       ")
        print("           =======       ")
        print()
        print("Has perdido")
    








# bandera = False
# while bandera:
#     os.system(0.1)
#     palabra = "madre"
#     intento = str(input("Dime una letra: "))
    
#     if intento == "m":
#         os.system(0.1)
#         print("*************************")
#         print("*** JUEGO EL AHORCADO ***")
#         print("*************************")
#         print("             !===N       ")
#         print("                 N       ")
#         print("                 N       ")
#         print("                 N       ")
#         print("           =======       ")
#         print()
#         print("         _ _ _ _ _       ")
#         print()
