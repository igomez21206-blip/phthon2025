import random  # Per generar números aleatoris

# -----------------------------
# Funció per crear llista de 20 elements aleatoris
# -----------------------------
def llista_20_elements():
    """
    Precondició: cap
    Postcondició: retorna una llista de 20 números aleatoris entre 1 i 100
    """
    return [random.randint(1, 100) for _ in range(20)]

# -----------------------------
# Funció per comprovar duplicats
# -----------------------------
def hi_ha_duplicats(llista):
    """
    Precondició: llista és una llista d'elements
    Postcondició: retorna True si hi ha algun element duplicat, False si no
    """
    return len(llista) != len(set(llista))

# -----------------------------
# Programa principal
# -----------------------------
# Generem la llista
llista = llista_20_elements()

# Mostrem la llista generada
print("Llista generada:")
print(llista)

# Comprovem si hi ha duplicats
if hi_ha_duplicats(llista):
    print("\nHi ha elements duplicats a la llista.")
else:
    print("\nNo hi ha elements duplicats a la llista.")
