print("============================")
print("COMPAÑÍA MULTINACIONAL RAPPI.")
print("============================")

nombre = str(input("\nPara comenzar, ingresa tu nombre: "))

print("\nHola " + nombre + ", bienvenido al programa que determina la cantidad de días de vacaciones que tendrás.")

print("\nA continuación, se presentan las claves de cada departamento:")

print("\n1. Departamento de Atención al Cliente (Clave 1)")
print("2. Departamento de Logística (Clave 2)")
print("3. Gerencia (Clave 3)")

dep = int(input("\nPara determinar tu sueldo, indica el NÚMERO de clave del departamento en el que trabajas: "))

if dep == 1:
    años_servicio = int(input("\nIngresa la cantidad de años de servicio que llevas en la compañía: \n"))

    if años_servicio == 1:
        print( nombre + ", te corresponden 6 días de vacaciones. Fin del programa.")
    if años_servicio >= 2 and años_servicio <= 6:
        print( nombre + ", te corresponden 14 días de vacaciones. Fin del programa.")
    if años_servicio >= 7:
        print( nombre + ", te corresponden 20 días de vacaciones. Fin del programa.")

if dep == 2:
    años_servicio = int(input("\nIngresa la cantidad de años de servicio que llevas en la compañía: \n"))

    if años_servicio == 1:
        print( nombre + ", te corresponden 7 días de vacaciones. Fin del programa.")
    if años_servicio >= 2 and años_servicio <= 6:
        print( nombre + ", te corresponden 15 días de vacaciones. Fin del programa.")
    if años_servicio >= 7:
        print( nombre + ", te corresponden 22 días de vacaciones. Fin del programa.")

if dep == 3:
    años_servicio = int(input("\nIngresa la cantidad de años de servicio que llevas en la compañía: \n"))

    if años_servicio == 1:
        print( nombre + ", te corresponden 10 días de vacaciones. Fin del programa.")
    if años_servicio >= 2 and años_servicio <= 6:
        print( nombre + ", te corresponden 20 días de vacaciones. Fin del programa.")
    if años_servicio >= 7:
        print( nombre + ", te corresponden 30 días de vacaciones. Fin del programa.")
  
