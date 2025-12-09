# -----------------------------
# Funció hi_ha_duplicats
# -----------------------------
def hi_ha_duplicats(llista):
    """
    Precondició: llista és una llista d'elements
    Postcondició: retorna True si hi ha algun element duplicat, False si no
    La llista original no es modifica.
    """
    return len(llista) != len(set(llista))  # si hi ha duplicats, el set serà més petit

# -----------------------------
# Proves
# -----------------------------
fruits1 = ["poma", "plàtan", "cirera", "mango"]
fruits2 = ["poma", "plàtan", "cirera", "poma"]

print("Fruits1:", fruits1, "-> Duplicats?", hi_ha_duplicats(fruits1))
print("Fruits2:", fruits2, "-> Duplicats?", hi_ha_duplicats(fruits2))