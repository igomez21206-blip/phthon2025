# -----------------------------
# Funció elimina_duplicats
# -----------------------------
def elimina_duplicats(llista):
    """
    Precondició: llista és una llista d'elements
    Postcondició: retorna una nova llista amb els elements únics de llista
    L'ordre dels elements originals es manté.
    """
    llista_nova = []
    for element in llista:
        if element not in llista_nova:
            llista_nova.append(element)
    return llista_nova

# -----------------------------
# Prova de la funció
# -----------------------------
fruits = ["poma", "plàtan", "cirera", "poma", "mango", "cirera"]

print("Llista original:", fruits)

# Eliminar duplicats
fruits_unics = elimina_duplicats(fruits)

print("Llista sense duplicats:", fruits_unics)