from clases.perro import Perro
from clases.gato import Gato
from clases.vaca import Vaca

# POLIMORFISMO: Capacidad de los objetos de diferentes clases de responder al mismo metodo de forma distinta


def hacer_sonido_de_animal(animal):
    print(f"{animal.nombre} hace {animal.hacer_sonido()}")

perro = Perro("Firulais")
gato = Gato("Pelusa")
vaca = Vaca("Lechera")

hacer_sonido_de_animal(perro) #guau
hacer_sonido_de_animal(gato) #miau
hacer_sonido_de_animal(vaca) #muuuu