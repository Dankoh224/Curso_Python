class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print('Hola, mi nombre es', self.nombre, self.apellido,'.')

usuario1 = Usuario('Danko', 'Valderrama')
usuario2 = Usuario('Camila', 'Oyarzun')

usuario1.saludo()

class Admin(Usuario):
    def super_saludo(self):
        print('Hola, soy',self.nombre, self.apellido, 'y soy administrador.')

administrador1 = Admin('Super','Administrador')
administrador1.saludo()
administrador1.super_saludo()