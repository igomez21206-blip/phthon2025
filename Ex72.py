import os

# 1. Crear el directori /home/cicles/AO/Prova
directori = "/home/cicles/AO/Prova"
os.makedirs(directori, exist_ok=True)  # exist_ok=True evita errors si ja existeix

# 2. Canviar-nos al directori creat
os.chdir(directori)

# 3. Crear el fitxer Ex12.txt amb els noms dels companys
companys = ["Anna", "Marc", "Laura", "Joan"]  # Exemple de noms de companys
with open("Ex12.txt", "w", encoding="utf-8") as fitxer:
    for nom in companys:
        fitxer.write(nom + "\n")

# 4. Obrir el fitxer per afegir els noms dels professors
professors = ["Sra. Pérez", "Sr. López"]  # Exemple de noms de professors
with open("Ex12.txt", "a", encoding="utf-8") as fitxer:
    for nom in professors:
        fitxer.write(nom + "\n")

# 5. Obrir el fitxer finalment i posar tot el seu contingut dins una llista
with open("Ex12.txt", "r", encoding="utf-8") as fitxer:
    llista_noms = [linia.strip() for linia in fitxer]  # strip() elimina salts de línia

print(llista_noms)
# Resultat: ['Anna', 'Marc', 'Laura', 'Joan', 'Sra. Pérez', 'Sr. López']