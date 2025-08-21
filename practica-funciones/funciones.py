# DECORADOR y WRAPPER

def decorador(funcion):
    def envoltorio():
        print("Esta funcionalidad se dispararia antes de la funcion que nos pasen por argumento")
        funcion()
        print("Esta funcionalidad se dispararia despues de la funcion que nos pasen por argumento")
    return envoltorio

def saludar():
    print("Hola, estoy saludando")

saludo_decorado = decorador(saludar)

saludo_decorado()