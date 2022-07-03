# Programa con una función que convierte segundos en horas, minutos y segundos. Pide los segundos y muestra el resultado:

def trans_segundos():
    segundos = int(input("Ingresa los segundos: "))
    horas = segundos // 3600
    minutos = segundos % 3600 // 60
    segundos =  segundos % 3600 % 60
    return horas, minutos, segundos

h, m, s = trans_segundos()
print(h,m,s)


