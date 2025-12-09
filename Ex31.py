# Sol·licitem les dades
any_actual = int(input("Introdueix l'any actual: "))

persones = []

for i in range(4):
    nom = input(f"Introdueix el nom de la persona {i+1}: ")
    any_naixement = int(input(f"Introdueix l'any de naixement de {nom}: "))
    edat = any_actual - any_naixement
    persones.append((nom, any_naixement, edat))
