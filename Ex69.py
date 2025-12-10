# Nombre de números
n = 10

# Potència desitjada
potencia = 2  # Pots canviar a 3, 4, etc.

# Llista dels números elevats a la potència
resultat = [
    i ** potencia
    for i in range(n)
]

print(resultat)