#1 Nombre del programa o equipo:

print("                                                  =============")
print("                                                  RECTANGUMAN")
print("                                                  =============\n")

#2 Interacción entre programa y usuario: Saludo y petición del nombre.

nombre = input("¡Hola! Bienvenido al programa que calcula el área de un rectángulo. ¿Cómo te llamas?: ") 

#3 Ingreso de datos del problema (continúa interacción).

largo = float(input("\nHola " + nombre + ". Para comenzar, ingresa el largo del rectángulo: "))
ancho = float(input("\nAhora ingresa el ancho del rectángulo: "))

#4 Resolución del problema.

area = largo * ancho

#5 Respuesta al usuario.

print("\n¡Listo! El área del rectángulo es de ",round(area)," unidades cuadradas.")

#6 Agradecimiento, fin y firma del programa o equipo.
print("\nGracias " + nombre + " por usar Rectanguman =)")
print("\nFin del programa.")
print("\n                                                  =============")
print("                                                  RECTANGUMAN")
print("                                                  =============\n")


