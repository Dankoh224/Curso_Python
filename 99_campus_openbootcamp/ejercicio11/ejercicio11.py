# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.
def anio_bisiesto(anio):
    if anio % 4 != 0 and anio % 100 != 0 and anio % 400 != 0:
        a = "El año NO es bisiesto"
    elif anio % 4 == 0 and anio % 100 != 0 and anio % 400 != 0:
        a = "El año SI es bisiesto"
    elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 != 0:
        a = "El año NO es bisiesto"
    elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 == 0:
        a = "El año SI es bisiesto"
    return a
print(anio_bisiesto(2400))



# Matemáticamente podemos saber si un año es bisiesto si este es múltiplo de 4. Si además es múltiplo de 100 no será bisiesto (ten en cuenta que 100 es múltiplo de 4 y por tanto cualquier número que sea múltiplo de 100 también es múltiplo de 4) a no ser que sea múltiplo de 400, que sí será bisiesto.