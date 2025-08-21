# -------------------------
# DICCIONARIO [Coleccion no ordenada de pares clave-valor]
# -------------------------

familia = {
    "padre": {
        "nombre": "Raul",
        "profesion": "Carpintero"
    },
    "madre": {
        "nombre": "Patricia",
        "profesion": "Abogada"
    },
    "hijo": {
        "nombre": "Pedro",
        "profesion": "Desempleado"
    }
}

for pariente, data in familia.items():
    print(pariente)

    for clave in data:
        print(clave + ":", data[clave])