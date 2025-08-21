from clases.mago import Mago


merlin = Mago("Merlin", ["Bola de fuego", "Rayo"])
gandalf = Mago("Gandalf", ["Llamar a las aguilas cuando termino la pelicula", "Bola de fuego"])

print(merlin) # devuelve el metodo __str__ que habiamos generado
print(len(merlin)) # devuelve el metodo __len__ que habiamos generado

print(gandalf) # devuelve el metodo __str__ que habiamos generado
print(len(gandalf)) # devuelve el metodo __len__ que habiamos generado

print(merlin == gandalf)

copia_merlin = Mago("Merlin", ["Bola de fuego", "Rayo"])

print(merlin == copia_merlin) # devuelve una comparacion usando los criterios que definimos en el metodo __eq__

mago_combinado = merlin + gandalf
print(mago_combinado)