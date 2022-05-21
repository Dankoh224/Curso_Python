print("0 1", end=" ")
x , y = 0 , 1

while y < 1597:
    z = x+y 
    print(z, end=" ")
    x , y = y , z

print("\n")
x = 0
y = 1

while y <= 1597:
    print(x,y, end=" ")
    x = x+y
    y = x+y
    

