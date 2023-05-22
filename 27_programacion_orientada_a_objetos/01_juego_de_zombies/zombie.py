# La ciudad se ha llenado de zombies. Estás en la calle 1 y has de llegar a la calle 40 para poder salvarte.
# Los zombies avanzan 1, 2, y 3 calles. Tu puedes avanzar 1, 2, y 3 calles.
# ¿Estás preparado, ¿cuál es tu nombre?
# El juego debe decir:
# Estás en la calle 1. Hay zonmbies en las calles 10, 12, 12, 14, 15, 16, 16, 17, 19 y 20.
# ¿Cuánto quieres correr? (1,2,3):
import random
class Zombie:
    
    def __init__(self):
        self.calle = random.randint(10,20)
        self.direccion = random.choice(['izquierda','derecha'])
        self.velocidad = random.randint(1,3)
    
    def moverse(self):
        if self.direccion == 'izquierda':
            self.calle -= self.velocidad
        else:
            self.calle += self.velocidad

    def no_visible(self):
        if self.calle < 1 or self.calle > 40:
            return True
        else:
            return False
        
