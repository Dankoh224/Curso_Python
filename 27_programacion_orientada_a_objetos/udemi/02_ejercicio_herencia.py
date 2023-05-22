class Animal():
    def __init__(self,nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    
    def saludo(self):
        print('Hola, mi nombre es {}. Soy un {} y {}.'.format(self.nombre,self.tipo, self.onomatopeya))

class Gato(Animal):
    tipo = 'gato'

class Perro(Animal):
    tipo = 'perro' 

gato1 = Gato('Don Gato','maullo')    
gato1.saludo()
perro1 = Perro('Scooby','ladro')    
perro1.saludo()