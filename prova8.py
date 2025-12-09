# Demanar dos números a l'usuari
v1 = int(input("Introdueix el 1r número: "))
v2 = int(input("Introdueix el 2n número: "))
# Calcular el resultat
r = v1 * v2

# Comprovar en quin interval està
if (25 <= r <= 30) or (105 <= r <= 125):
    print("El resultat està entre 25 i 30 o entre 105 i 125")
elif 55 <= r <= 60:
    print("El resultat està entre 55 i 60")
else:
    print("No està en els intervals demanats")