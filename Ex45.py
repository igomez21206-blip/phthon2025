# Programa per sumar els dígits d'un número i indicar si la suma és parell o senar

# Funció per demanar un número enter
def demanar_numero(missatge):
    while True:
        try:
            num = int(input(missatge))
            return num
        except ValueError:
            print("Error: introdueix un número enter vàlid.")

# -----------------------------
# Programa principal
# -----------------------------

# Demanar el número a l'usuari
numero = demanar_numero("Introdueix un número: ")

# Convertir el número a positiu per sumar els dígits
numero_abs = abs(numero)

# Calcular la suma dels dígits
suma_digits = sum(int(digit) for digit in str(numero_abs))

# Mostrar la suma
print(f"\nSuma dels dígits de {numero}: {suma_digits}")

# Comprovar si la suma és parell o senar
if suma_digits % 2 == 0:
    print("La suma és parell.")
else:
    print("La suma és senar.")