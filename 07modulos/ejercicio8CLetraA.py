# Programa que lleva a cabo una cuenta atrás de 10 segundos:
# 1) Muestra cada segundo (10, 9, 8,...)
# 2) Muestra cada 5 décimas de segundo (10, 9.5, 9, 8.5,...)
# Mide el tiempo para comprobrar que transcurren 10 segundos.
import time
inicio = time.time()
for i in range (1,12):
    print(11-i)
    if i == 11:
        break
    time.sleep(1)
final = time.time()
print(final-inicio)