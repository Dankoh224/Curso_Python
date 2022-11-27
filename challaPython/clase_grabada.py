

lista_estudiantes = [0,1,2,3,4,5,6,7,8,9]

nombre = "Catalina Cortéz Díaz"
arte = ["tocar guitarra","piano","batería","cantar","baile","dibujo y pintar","actriz","cocina internacional","fotografía"]
ciencia = ["medicina","pediatría","odontología","programación","arquitectura","contabilidad","astronomía","ingeniería espacial","derecho","veterinaria"]
gustos = ["medicina", "pediatría", "derecho", "viajar"]
print(nombre)
print("Sus gustos son:")
for i in range(len(gustos)):
    print(gustos[i])
puntaje_arte= 0
puntaje_ciencia = 0
puntaje_ciencia_arte = 0
for i in gustos:
    if i in arte and i in ciencia:
        puntaje_ciencia_arte += 1
    elif i in arte:
        puntaje_arte += 1
    elif i in ciencia:
        puntaje_ciencia += 1
if puntaje_ciencia>= 1 and puntaje_arte >= 1:
    print("El alumno prefiere las ciencias y las artes")
elif puntaje_ciencia >= 1:
    print("El alumno prefiere las ciencias")
elif puntaje_arte >= 1:
    print("El alumno prefiere las artes")

