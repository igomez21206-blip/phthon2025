# Demanar la quantitat inicial amb validació
while True:
    try:
        cinicial = float(input("Introdueix la quantitat a sol·licitar (50.000€ - 800.000€): "))
        if 50000 <= cinicial <= 800000:
            break
        else:
            print("La quantitat ha d'estar entre 50.000€ i 800.000€.")
    except ValueError:
        print("Si us plau, introdueix un número vàlid.")

# Demanar l'interès amb validació
while True:
    try:
        interès = float(input("Introdueix l'interès (%) (0.5% - 13%): "))
        if 0.5 <= interès <= 13:
            break
        else:
            print("L'interès ha d'estar entre 0.5% i 13%.")
    except ValueError:
        print("Si us plau, introdueix un número vàlid.")

# Demanar el número d'anys amb validació
while True:
    try:
        anys = int(input("Introdueix el número d'anys (3 - 40): "))
        if 3 <= anys <= 40:
            break
        else:
            print("Els anys han d'estar entre 3 i 40.")
    except ValueError:
        print("Si us plau, introdueix un número enter.")

# Calcular el capital final
cfinal = cinicial * (1 + interès/100) ** anys

# Mostrar el resultat amb 2 decimals
print(f"El capital final serà: {cfinal:.2f}€")
