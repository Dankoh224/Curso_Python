# Método format con símbolo % (ya no se usa pero puede aparecer por algun proyecto)
nombre = "luna"
edad = 10

print("Nuestra perrita se llama",nombre,"y tiene",edad,"años." )
print("Nuestra perrita se llama {} y tiene {} años.".format(nombre,edad))
print("Nuestra perrita se llama %s y tiene %s años." % (nombre,edad))

# Si queremos que una variable cambie a un tipo haremos lo siguiente:
print("Nuestra perrita se llama",nombre,"y tiene",float(edad),"años." )
print("Nuestra perrita se llama {} y tiene {:f} años.".format(nombre,edad))
print("Nuestra perrita se llama %s y tiene %f años." % (nombre,edad))

# Si queremos menos decimales:
print("Nuestra perrita se llama",nombre,"y tiene",edad,"años." )
print("Nuestra perrita se llama {} y tiene {:.2f} años.".format(nombre,edad))
print("Nuestra perrita se llama %s y tiene %.2f años." % (nombre,edad))

# Reservar espacio e iniciar en la derecha:
print("Nuestra perrita se llama",nombre,"y tiene",edad,"años." )
print("Nuestra perrita se llama {} y tiene {:20} años.".format(nombre,edad))
print("Nuestra perrita se llama %s y tiene %20s años." % (nombre,edad))

# Reservar espacio e iniciar en la izquierda:
print("Nuestra perrita se llama {} y tiene {:<20} años.".format(nombre,edad))
print("Nuestra perrita se llama %s y tiene %-20s años." % (nombre,edad))

# SOLO método format reserva espacio en el centro:
print("Nuestra perrita se llama {} y tiene {:^20} años.".format(nombre,edad))

# También podemos usar los datos dentro de diccionarios y para esto lo haremos de la siguiente forma:
datos = {"producto": "patatas", "precio": 5}
print("Precio de %(producto)s es %(precio)s euros" % datos)
print("Precio de {d[producto]} es {d[precio]} euros.".format(d=datos))
print("Precio de {n} es {m} euros.".format(n=datos["producto"],m=datos["precio"]))
print("Precio de {producto} es {precio} euros.".format(**datos))