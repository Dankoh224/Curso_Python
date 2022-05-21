#1 Nombre del programa o equipo:

print("                      =======================================")
print("                     ÁREA Y PERÍMETRO DE TRIÁNGULOS RECTÁNGULOS")
print("                     ========================================\n")

#2 Interacción entre programa y usuario: Saludo y petición del nombre.

nombre = input("¡Hola! Bienvenido al programa que calcula el área y perímetro de un triángulo rectángulo. ¿Cómo te llamas?: ") 

#3 Ingreso de datos del problema (continúa interacción).

cateto1 = float(input("\nHola " + nombre + ". Para comenzar, ingresa la medida del primer cateto del triángulo rectángulo: "))
cateto2 = float(input("\nAhora ingresa la medida el segundo cateto del triángulo rectángulo: "))

#4 Resolución del problema.

area = (cateto1 * cateto2) / 2
perimetro = (cateto1**2+cateto2**2)**(0.5) + cateto1 + cateto2 

#5 Respuesta al usuario.

print("\n¡Listo! El área del rectángulo es de ", area," unidades cuadradas. Y el perímetro es de ", perimetro, " unidades.")

#6 Agradecimiento, fin y firma del programa o equipo.
      
print("\nGracias " + nombre + " por usar Área y Perímetros de Triángulos Rectángulos =)")
print("\nFin del programa.")
print("\n                      =======================================")
print("                     ÁREA Y PERÍMETRO DE TRIÁNGULOS RECTÁNGULOS")
print("                     ========================================\n")


