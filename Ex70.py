def dividir(a, b):
    """
    Retorna el resultat de dividir a entre b.
    Si b és 0, avisa que no es pot dividir per zero.
    """
    if b == 0:
        print("Error: no es pot dividir per zero.")
        return None
    else:
        return a / b

# Exemples d'ús
print(dividir(10, 2))  # Resultat: 5.0
print(dividir(10, 0))  # Mostra l'avís i retorna None