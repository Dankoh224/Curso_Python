x = int(input("ingrese un numero positivo"))
total_pares = 0
total_impares = 0
while x != 0:
    par = 0
    impar = 0
    while x > 0:
        if (x % 10) % 2 == 0:
            par = par + 1
            total_pares = total_pares + 1
            x = x//10
        else:
            impar = impar + 1
            total_impares = total_impares + 1
            x = x//10

    print("Hay un total de " , par , "números pares y " , impar , " números impares en este número.")
    x = int(input("ingrese el siguiente numero positivo"))

print("Hay un total de " , total_pares , "números pares y " , total_impares , " números impares entre todos los valores que ingresaste.")

