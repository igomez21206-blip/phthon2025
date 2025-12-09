# Programa per convertir números binaris a enters

# Demanem a l'usuari un número binari
binari = input("Introdueix un número binari: ")

# Convertim el número binari a enter utilitzant la funció int()
enter = int(binari, 2)  # La base 2 indica que és binari

# Mostrem el resultat
print(f"El número binari {binari} és {enter} en decimal.")