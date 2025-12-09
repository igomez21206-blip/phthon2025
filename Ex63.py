def paraules_per_lletra(llista, lletra):
    """
    Retorna una llista amb les paraules de 'llista' que comencen per la lletra 'lletra'.
    La comparació és sensible a majúscules/minúscules.
    """
    return list(filter(lambda paraula: paraula.startswith(lletra), llista))

# Exemple de prova
paraules = ["maria", "manta", "peu", "mà"]
resultat = paraules_per_lletra(paraules, "p")
print(resultat)