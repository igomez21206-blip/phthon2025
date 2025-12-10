def compta_coincidencies(llista):
    return sum(1 for i, valor in enumerate(llista) if i == valor)

# Exemple d'ús:
numeros = [0, 2, 3, 3, 4]
resultat = compta_coincidencies(numeros)
print(resultat)  # Imprimeix: 3