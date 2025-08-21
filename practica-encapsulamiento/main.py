from clases.cuenta_bancaria import CuentaBancaria

# Creamos instancia
cuenta = CuentaBancaria("Ramiro Cafferata", 1000)

# Obtener saldo inicial
print(cuenta.obtener_saldo())

# Afregar $500 y volver a obtener saldo
cuenta.depositar(-500)
print(cuenta.obtener_saldo())

# Retirar $1000 y volver a obtener saldo
cuenta.retirar(1500)
print(cuenta.obtener_saldo())