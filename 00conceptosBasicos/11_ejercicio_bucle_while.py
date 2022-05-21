# 1) Escriba un programa que pregunte una y otra vez si desea continuar con el programa, siempre que se conteste exactamente sí (en minúsculas y con tilde).
print("Ejercicio 1:")
x = str(input('¿Desea continuar con el programa? Escriba "sí", si desea continuar: '))

while x == "sí":
    x = str(input('¿Desea continuar con el programa? Escriba "sí", si desea continuar: '))

# 2) Escriba un programa que pregunte una y otra vez si desea terminar el programa, salvo si se contesta exactamente SI (en mayúsculas y sin tilde).
print("Ejercicio 2:")
x = str(input('¿Desea terminar el programa? Escriba "SI", si desea terminar: '))

while x != "SI":
    x = str(input('¿Desea terminar el programa? Escriba "SI", si desea terminar: '))

# 3) Escriba un programa que pregunte una y otra vez si desea terminar el programa, siempre que se conteste exactamente N (en mayúsculas).
print("Ejercicio 3:")
x = str(input('¿Desea terminar el programa? Escriba cualquier valor menos "N", si desea finalizar: '))

while x == "N":
    x = str(input('¿Desea terminar el programa? Escriba cualquier valor menos "N", si desea finalizar: '))

# 4) Escriba un programa que pregunte una y otra vez si desea continuar el programa, salvo si se contesta exactamente no (en minúsculas).
print("Ejercicio 4:")
x = str(input('¿Desea continuar el programa? Escriba "no", si desea finalizar: '))

while x != "no":
    x = str(input('¿Desea continuar el programa? Escriba "no", si desea finalizar: '))

# 5) Escriba un programa que pregunte una y otra vez si desea continuar con el programa, siempre que se conteste S o s (en mayúsculas o en minúsculas).
print("Ejercicio 5:")
x = str(input('¿Desea continuar el programa? Escriba "S o s", si desea continuar: '))

while x == "s" or x == "S":
    x = str(input('¿Desea continuar el programa? Escriba "S o s", si desea continuar: '))

#6) Escriba un programa que pregunte una y otra vez si desea terminar el programa, salvo si se contesta S o s (en mayúsculas o en minúsculas).
print("Ejercicio 6:")
x = str(input('¿Desea terminar el programa? Escriba cualquier valor menos "S o s", si desea terminar: '))

while x == "s" or x == "S":
    x = str(input('¿Desea terminar el programa? Escriba cualquier valor menos "S o s", si desea terminar: '))


