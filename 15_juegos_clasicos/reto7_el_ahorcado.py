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

contadorIncorrectas = 0
contadorCorrectas = 0
# Paso 1: Obtener una palabra a adivinar.
listaPalabras = ["perro","escalera","hipopotamo","cordillera","petardo","continente","hipotalamo","chispa"]
palabraAdivinar = listaPalabras[random.randint(0,len(listaPalabras))]
listaNueva = list(palabraAdivinar)
os.system("cls")

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
guiones = []
for i in palabraAdivinar:
    guiones.append("_")
separador = " "
print(separador.join(guiones))

bandera = True
while bandera:

    # Paso 4: Pedir al usuario que introduzca una letra. Si no es una única letra indicarlo. Si ya se ha dicho indicarlo.

    banderaLetra = True
    while banderaLetra:
        letra = str(input("Ingrese una letra: "))
        if len(letra) != 1:
            print("Ingrese solo una letra.")
        elif letra in "0123456789":
            print("No puede ingresar números.")
        else:
            banderaLetra = False
    
    os.system("cls")

    # 5. Comprobar si esa letra está contenida en la palabra elegida.
    # 6. Si está: Volver a mostrar el dibujo de la horca como la última vez. Sustituir el guión correspodiente por la letra dicha.
    # 7. Si no está: Mostrar el dibujo de la horca al que se añade una parte. Volver a mostrar los guiones como la última vez.

    if letra not in palabraAdivinar or letra in guiones:
        contadorIncorrectas += 1
        print("Letra incorrecta. Tiene 6 intentos. Lleva {}".format(contadorIncorrectas))
    else:
        # En estas líneas guardaremos las letras en una lista e imprimiremos.
        for i in range(0,len(palabraAdivinar)):
            if letra == palabraAdivinar[i]:
                guiones.pop(i)
                guiones.insert(i,palabraAdivinar[i])
    
    if contadorIncorrectas == 0:
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
    if contadorIncorrectas == 1:
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
    elif contadorIncorrectas == 2:
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
    elif contadorIncorrectas == 3:
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
    elif contadorIncorrectas == 4:
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
    elif contadorIncorrectas == 5:
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
    elif contadorIncorrectas == 6:
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

    separador = " "
    print(separador.join(guiones))

    if contadorIncorrectas == 6:
        print("¡¡O no!! Lo sentimos, has perdido.")
        bandera = False
    if listaNueva == guiones:
        print("¡¡Waaaauuu!! ¡¡Has acertado!! ¡¡Ganaste!!")
        bandera = False
