#crear instancias de la clase perro
from clases.perro import Perro

perro1 = Perro ("Firulais", 3) # esta llamando por detras al constructor pasandole nombre y edad
perro2 = Perro ("Luna", 5) # esta llamando por detras al constructor pasandole nombre y edad

# -----------------------------------------------

# Usando template strings con las variables propias de la instancia de una clase (objeto)
print(f"{perro1.nombre} tiene {perro1.edad} años y dice {perro1.ladrar()}")
print(f"{perro2.nombre} tiene {perro2.edad} años y dice {perro2.ladrar()}")