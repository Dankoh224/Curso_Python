# Hacer una copia de una lista anidada.
p = [1,[2,3],[4,5,6]]
a = p[0]
b = list(p[1])
c = list(p[2])
q = [a,b,c]
print(p)
print(q)
print()
print(id(p))
print(id(q))
p[0] = 20
q[0] = 20
print(p)
print(q)
print()
for i in p:
    print(id(i))
print()
for i in q:
    print(id(i))

# Otra forma de hacer una copia de una lista anidada:
r = [p[0],list(p[1]),list(p[2])]
print(r)
# Y otra forma más:
s = [p[0]] + [list(p[1])] + [list(p[2])]
print(s)
print(id(r))
print(id(s))

# Y otra más:
t = [p[0],p[1][:],p[2][:]]
print(t)
print(id(t))

# Finalmente, el comando para hacer esto directamente es:
import copy
m = [1,[2,[3,4,5]]]
n = copy.deepcopy(m)
m[0] = 15
print(m)
print(n)
print(id(m[1][1]))
print(id(n[1][1]))
# Esto es un comentario