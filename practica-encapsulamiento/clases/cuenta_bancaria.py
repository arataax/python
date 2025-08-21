class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular # Usando __ dos guiones hacemos privado el atributo
        self.__saldo = saldo_inicial


    # Setter (editor, configurador)
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Deposito de ${cantidad} exitoso!")
        else:
            print("Error: la cantidad a depositar debe ser mayor a cero")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Se ha retirado ${cantidad} exitosamente!")
        else:
            print("Fondos insuficientes o cantidad invalida")

    # Getter (obtener informacion privada a a traves de un  metodo publico)

    def obtener_saldo(self):
        return f"El saldo actual de la cuenta es ${self.__saldo}"