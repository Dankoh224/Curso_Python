# Haz un programa que elimine todos los meses que tengan la latra b.
from os import remove


meses = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
mesesCopia = list(meses)
for i in mesesCopia:
    if "b" in i:
        meses.remove(i)
print(meses)

# Forma 2
meses = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
for i in range(len(meses)-1,-1,-1):
    if "b" in meses[i]:
        meses.remove(meses[i])
print(meses)
