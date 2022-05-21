# Programa que muestre los numeros del 1 al 100 con range() y bucles for.
# Luego muestre del 1 al 100 usando el salto (tercer argumento) y bucles for.
# Luego que muestre del 100 al 1 con range() y bucles for.
# Finalmente que muestre del 100 al 1 usando salto y bucles for.
for i in range(0,10):
    for j in range(1,11):
        print("{:2} ".format(i*10+j), end = "")
    print()

print()
print()

for i in range(0,91,10):
    for j in range(1,11):
        print("{:2} ".format(i+j), end = "")
    print()

print()
print()

for i in range(90,-1,-10):
    for j in range(10,0,-1):
        print("{:3} ".format(i+j), end = "")
    print()

print()
print()

for i in range(10,0,-1):
    for j in range(0,10):
        print("{:3} ".format(i*10-j), end = "")
    print()