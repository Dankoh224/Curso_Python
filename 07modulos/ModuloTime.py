# Otro módulo muy importante para juegos y aplicaciones es el módulo time. Primero vamos a importarlo:
import time
# Aquí podemos ver todas las funciones que se encuentran en este módulo:
print(dir(time))
# Y aquí veremos en especial la función TIME y en esta oportunidad, veremos que al imprimir time.time() aparece la cantidad de segundos que han pasado desde 1970 hasta este momento.
print(time.time())

# Si nosotros dividimos en 60 para hallar minutos, por 60 para hallar horas, por 24 para hallar días, por 365.6 para hallar años y a eso le sumamos 1970, el resultado que obtendremos será exactamente el año en el que nos encontramos:

print(time.time()/60/60/24/365.6+1970)

# Ahora veremos un pequeño "juego" para usar esta función.

inicio = time.time() # El pc tomará los segundos que han transcurrido desde 1970 en el momento que leyó esta línea de código.
while True:
    print("Estamos jugando...")
    final = time.time() # El pc contabilizará los segundos que han transcurrido desde 1970 hasta esta línea de código.
    if final - inicio >= 3: # Al hacer esta resta, podemos tener el tiempo transcurrido entre inicio y final.
        break # Y esta línea para terminar el bucle.
print("Han pasado",(final-inicio)//1,"segundos.") # Aquí, he dividido usando la división parte entera, para que dé el segundo exacto, una cosa de vistosidad.

# Función Sleep: Es una función que sirve para que nuestro programa esté en modo durmiendo los segundos que le demos como argumento. Ejemplo:
print("Inicio del programa")
inicio = time.time()
time.sleep(3)
final = time.time()
total = final - inicio
print("Final del Programa.")
print("El tiempo que el programa estuvo detenido es de {} segundos.".format(total))