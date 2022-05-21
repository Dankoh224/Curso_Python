# Comprobar cuántas veces aparece el carácter "o", con o sin tilde, en la siguiente cadena de carácteres:
a = "Muchos años después, frente al pelotón de fusilamiento, el coronel Aureliano Buendía había de recordar aquella tarde remota en que su padre lo llevó a conocer el hielo"
n = 0
total = 0 
while n <= len(a) - 1:
    if a[n] == "o" or a[n] == "ó" or a[n] == "O" or a[n] == "Ó":
        total = total + 1
    n = n + 1
print("Existen {} os en la cadena de carácteres.".format(total))