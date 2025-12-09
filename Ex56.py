def suma_interval(a, b):
    suma = 0
    for i in range(a, b + 1):
        suma += i
    return suma

# Exemple de prova
inici = 3
fi = 7
resultat = suma_interval(inici, fi)
print(f"La suma dels números entre {inici} i {fi} és: {resultat}")
