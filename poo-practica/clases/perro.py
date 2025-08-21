#Definiendo la clase (plantilla)
class Perro:
    #metodo constructor (__init__)
    def __init__(self, nombre, edad):
        self.nombre = nombre # Al atributo nombre de la instancia le asignamos "nombre" que nos envian como argumento en el constructor
        self.edad = edad # Al atributo edad de la instancia le asignamos "edad" que nos envian como argumento en el constructor

    def ladrar(self):
        return "Guau!"