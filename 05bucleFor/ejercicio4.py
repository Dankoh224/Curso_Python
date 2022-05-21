#Tenemos una tupla con los meses del año. Queremos saber qué meses tienen en su nombre la letra b.
meses = ("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre") 
for i in meses:
    if "b" in i:
        print("El mes {} tiene la letra b en su nombre.".format(i))

# Este ejercicio permite que CADA DATO SEA REVISADO condicionándolo para ser guardado en una tupla o lista:
tuplaDeMeses = ()
print(type(tuplaDeMeses))
for i in meses:
    if "b" in i:
        tuplaDeMeses += (i,) 
print(tuplaDeMeses)
# IMPORTANTE: NO OLVIDAR que detrás de la variable va la coma, así se identifica como TUPLA y no como CADENA DE CARACTERES (si quieres listas cambia los paréntesis por corchetes).