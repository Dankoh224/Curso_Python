# Las funciones sin parámetros en python devuelven nada, es decir, devuelven la sentencia NONE. Sin embargo, imprimen inmediatamente lo que aparece en pantalla.
def pantallaInicio ():
    
    print("***********************************")
    print("*                                 *")
    print("*      PANTALLA DE INICIO         *")
    print("*                                 *")
    print("*    Bienvenidos al sistema       *")
    print("*                                 *")
    print("***********************************")

    return None

# Aquí llamamos la función para que se imprima:
pantallaInicio()

# Y acá llamamos al return de la función, lo que nos devolverá None:
print(pantallaInicio())