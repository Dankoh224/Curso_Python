# Tenemos una lista de números y queremos separar los pares de los impares y guardarlos en otras dos listas. Hazlo con el método append.
numeros = [2,3,5,8,9,12,21,24,25,28]
par = []
impar = []
for i in numeros:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
print("Lista 1: {}".format(par))
print("Lista 2: {}".format(impar))