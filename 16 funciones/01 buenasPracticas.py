#Si nosotros usamos una función como la del siguiente ejemplo:
def sumar (sumando1,sumando2):
    print(sumando1+sumando2)
# Cuando llamemos a la función, esta funcionará correctamente:
sumar(3,2)
# Sin embargo, esta función realiza dos tareas, UNA es calcular la suma
# y la OTRA es mostrarla en pantalla. Sin embargo, conviene que la función solo
# realicen una tarea. Además, no podremos tener ese resultado guardado en niguna
# variable, por lo tanto no podríamos operar con ese resultado, asi que sería mejor,
# que en vez de un print, usemos un return:
def sumar (sumando1,sumando2):
    return sumando1+sumando2
print(sumar(2,4))
# Y aquí lo de operar con la función y su resultado:
print(sumar(3,3) + sumar(3,8))