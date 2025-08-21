from clases.heroe import Heroe
from clases.villano import Villano


superman = Heroe("Superman", 100, "Volar")
joker = Villano("Joker", 80, "Robar Bancos")

#-------------------------------------------------------

superman.identificarse() # Heredado
superman.mostrar_salud() # Heredado

superman.mostrar_poder() # Medodo (comportamento) propio de heroe

joker.identificarse() # Heredado
joker.mostrar_salud() # Heredado

joker.mostrar_habilidad() # Medodo (comportamento) propio de villano
