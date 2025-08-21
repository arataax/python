import random


class Enemigo:
    def __init__(self, nombre, salud, damage):
        self.nombre = nombre
        self.salud = salud
        self.damage = damage

    def atacar(self):
        return random.randint(5,15)
    
    def recibir_damage(self, damage):
        self.salud -= damage
        if self.salud <= 0 :
            print(f"Has derrotado a {self.nombre}!")
            return True
        return False