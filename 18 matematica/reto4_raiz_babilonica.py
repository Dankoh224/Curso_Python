# Raíz babilónica:

from re import X

a = 200
def raiz(n):
    x = n/2
    for i in range(30):
        if x*x == n:
            return x
        else:
            copia_x = x
            x = (x+n/x)/2
            
        if copia_x == x:
            break
    return x
print(raiz(a))