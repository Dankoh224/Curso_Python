# Programa que permite convertir unidades de masa: kilogramos a libras y libras a 
# kilogramos (1 kg = 2.20462262 lbs y 1lb = 1/2.20462262 kg)
def kilo_a_Libra (kgr):
    return kgr*2.20462262

def libra_a_Kilo (libra):
    return libra*(1/2.20462262)

kgr = float(input("Ingrese la cantidad de kilogramos: "))
libra = float(input("Ingrese la cantidad de libras: "))

print(kgr,"kilos es equivalente a",kilo_a_Libra(kgr),"libras.")
print(libra,"libras es equivalente a ",libra_a_Kilo(libra),"kilos.")