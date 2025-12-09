# Programa per imprimir la taula de multiplicar d'un número

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
# Programa principal
# -----------------------------

# Demanar el número per la taula de multiplicar
numero = demanar_numero(
    "Introdueix un número per la taula de multiplicar (1 - 20): ",
    1, 20
)

# Imprimir la taula de multiplicar
print(f"\nTaula de multiplicar del {numero}:")
print("-" * 25)

for i in range(1, 11):  # De l'1 al 10
    resultat = numero * i
    print(f"{numero} x {i:2} = {resultat:3}")

print("-" * 25)