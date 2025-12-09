def llegir_frases(n):
    """
    Precondició: n és un número enter
    Postcondició: retorna una llista amb n frases llegides del teclat
    """
    llista = []
    for i in range(n):
        frase = input(f"Introdueix la frase {i+1}: ")
        llista.append(frase)
    return llista

def convertir_majuscules(frase):
    """
    Precondició: frase és una cadena de text
    Postcondició: retorna la frase amb les consonants en majúscula
    """
    vocals = "aeiouAEIOU"
    resultat = ""
    
    for lletra in frase:
        if lletra.isalpha() and lletra not in vocals:  # consonant
            resultat += lletra.upper()
        else:
            resultat += lletra
    return resultat

def escriure_frases(llista):
    """
    Precondició: llista és una llista de frases
    Postcondició: imprimeix cada frase de la llista
    """
    print("\nFrases modificades:")
    for frase in llista:
        print(frase)

# -----------------------------
# Programa principal
# -----------------------------

# Llegir el número de frases
n = int(input("Introdueix el nombre de frases: "))

# Llegir les frases
frases = llegir_frases(n)

# Convertir les consonants en majúscula per cada frase
frases_modificades = [convertir_majuscules(frase) for frase in frases]

# Imprimir les frases modificades
escriure_frases(frases_modificades)