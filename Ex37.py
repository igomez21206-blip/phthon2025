import random
import time

# Funció on expliquem què passa
def intro():
    print("""En una època on els gegants governen Menorca. Nosaltres necessitem menjar.
Estem seguint el rastre de l'olor del menjar, però ens trobem en una cruïlla.
Al final de cada camí hi ha un talaiot: en un viuen els gegants bons que ens convidaran,
i en l'altre hi ha caníbals afamats que ens menjaran tan bon punt ens vegin.
""")

# Funció on demanem a quin talaiot volem anar
def canviTalaiot():
    talaiot = ""
    while talaiot != "1" and talaiot != "2":
        talaiot = input("A quin Talaiot vols anar? Introdueix 1 o 2: ")
    return talaiot

# Funció que determina si guanyes o perds
def trobada(opcio_usuari):
    print("T'estàs apropant al talaiot...")
    time.sleep(1.5)
    print("Està fosc i és tenebrós...")
    time.sleep(1.5)
    print("Un gran gegant salta davant teu, t'agafa i ...\n")
    time.sleep(1.5)

    gegantamic = random.randint(1, 2)

    if opcio_usuari == str(gegantamic):
        print("Et convida a menjar!\nHas guanyat aquesta ronda!\n")
        return True
    else:
        print("Se't menja d'un mos... ÑAM ÑAM ÑAM\n")
        return False


# Programa principal amb sistema de punts
punts = 0
partidaNova = "si"

while partidaNova == "si" or partidaNova == "s":
    intro()
    opcio = canviTalaiot()
    resultat = trobada(opcio)

    if resultat:
        punts += 1
        print(f"Punts actuals: {punts}\n")
    else:
        print("Has perdut la partida!")
        break

    partidaNova = input("Vols tornar a menjar (jugar)? Introdueix si o no: ").lower()
    print("\n")

print(f"Punts totals aconseguits: {punts}")
print("Gràcies per jugar!")