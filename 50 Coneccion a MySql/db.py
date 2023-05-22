import mysql.connector

midb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password ='dynavolt11',
    database = 'prueba'
)

# CURSOR:
cursor = midb.cursor()
# Un cursor es un objeto que nos permite interactuar con la base de datos
# mediante el lenguaje SQL. A este cursor podemos darle el método execute
# para realizar consultas'''
cursor.execute('select * from Usuario')
# sin embargo hay que pedirle que nos devuelva los datos, así que guardaremos esto
# en una variable llamada resultado

# NOTA: si no queremos todos los resultados podemos agregar la palabra limit
# seguida de la cantidad de elementos que queremos limitar. Ej:
# cursor.execute('select * from Usuario limit 2')

# Cursor para MOSTRAR EL DETALLE de la tabla Usuario:
# cursor.execute('show create table Usuario')

# Cursor para INSERTAR datos:
#sql = 'insert into Usuario (email, username, edad) values(%s,%s,%s)'
#values = ('micorreo@correo.co.nz', 'nombreusuario', 45)
#cursor.execute(sql,values)
#midb.commit()
#print(cursor.rowcount)


#Cursor para ACTUALIZAR datos:
# sql = 'update Usuario set email = %s where id = %s'
# values = ('micorreo@correo.com', 3)
# cursor.execute(sql,values)
# midb.commit()
#print(cursor.rowcount)


#Cursor para ELIMINAR datos:
# sql = 'delete from Usuario where id = %s'
# values = (3, )
# cursor.execute(sql,values)
# midb.commit()
#print(cursor.rowcount)


resultado = cursor.fetchall()
print(resultado)