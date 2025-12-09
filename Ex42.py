# Programa per calcular la quantitat de dígits d'un número

# Funció per demanar un número dins d'un rang
def demanar_numero(missatge, min_valor, max_valor):
    while True:
        try:
            num = int(input(missatge))
            if min_valor <= num <= max_valor:
                return num
            else:
                print(f"Error: el número ha d'estar entre {min_valor} i {max_valor}.")
        except ValueError:
            print("Error: introdueix un número vàlid.")

# -----------------------------
# Dades d'entrada
# -----------------------------
numero = demanar_numero(
    "Introdueix un número (1 - 900000): ", 
    1, 900000
)

# -----------------------------
# Càlcul de la quantitat de dígits
# -----------------------------
# Convertim el número a string i comptem els caràcters
num_digits = len(str(numero))

# -----------------------------
# Resultat
# -----------------------------
print("\n--------- Resultat ---------")
print(f"El número introduït és: {numero}")
print(f"Quantitat de dígits: {num_digits}")
print("----------------------------")