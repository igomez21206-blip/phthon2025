# Demanar un número
numero = int(input("Introdueix un número: "))

# Mostrar només els dígits parells
print("Dígits parells:", end=" ")
for digit in str(abs(numero)):
    if int(digit) % 2 == 0:
        print(digit, end=" ")