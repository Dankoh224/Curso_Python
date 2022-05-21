# Programa que lleva a cabo una cuenta atrás de 10 segundos:
# 1) Muestra cada segundo (10, 9, 8,...)
# 2) Muestra cada 5 décimas de segundo (10, 9.5, 9, 8.5,...)
# Mide el tiempo para comprobrar que transcurren 10 segundos.
import time
tiempo = True
contador = 10
print(contador)
inicioReal = time.time()
while tiempo:
    inicio = time.time()
    time.sleep(.5)
    final = time.time()
    contador -= .5
    temporizador = contador - (final-inicio)//1
    print(temporizador)
    
    if temporizador <= 0:
        finalReal = time.time()
        break
print("Transcurrieron {} segundos en total.".format(finalReal-inicioReal))