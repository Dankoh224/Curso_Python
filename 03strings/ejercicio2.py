# Mostrar en pantalla las letras que forman la palabra "mariposa".
a = "mariposa "
ingresar = True
n = 0
while ingresar:
    if n <= len(a) - 1:
        print(a[n])
        n = n + 1
    else:
        ingresar = False