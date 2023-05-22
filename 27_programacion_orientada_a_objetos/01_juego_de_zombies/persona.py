# La ciudad se ha llenado de zombies. Estás en la calle 1 y has de llegar a la calle 40 para poder salvarte.
# Los zombies avanzan 1, 2, y 3 calles. Tu puedes avanzar 1, 2, y 3 calles.
# ¿Estás preparado, ¿cuál es tu nombre?

class Persona:
    def __init__(self,nombre):
        self.nombre = nombre
        self.calle = 1

    def situacion(self):
        return '{}, estás en la calle {}.'.format(self.nombre, self.calle)
    
    def moverse(self, velocidad):
        if velocidad == "1":
            self.calle += 1
            return self.calle
        elif velocidad == "2":
            self.calle += 2
            return self.calle
        else:
            self.calle += 3
            return self.calle
