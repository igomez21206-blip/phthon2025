# -----------------------------
# Funció esta_ordenada
# -----------------------------
def esta_ordenada(llista):
    """
    Precondició: llista és una llista de números
    Postcondició: retorna un missatge indicant si la llista està ordenada
                  de forma ascendent, descendent o no està ordenada
    """
    if llista == sorted(llista):
        return "Està ordenada de forma ascendent"
    elif llista == sorted(llista, reverse=True):
        return "Està ordenada de forma descendent"
    else:
        return "No està ordenada"

# -----------------------------
# Proves
# -----------------------------
print(esta_ordenada([3, 2, 1]))  # descendent
print(esta_ordenada([4, 5, 6]))  # ascendent
print(esta_ordenada([1, 3, 2]))  # no ordenada