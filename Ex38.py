import random

# Funció per generar un codi de 4 xifres
def generar_codi():
    return [random.randint(0, 9) for _ in range(4)]

# Funció per avaluar un intent
def avaluar_intent(codi, intent):
    encertats = 0
    coincideixen = 0

    # Comptem encertats (mateix número i posició)
    for i in range(4):
        if intent[i] == codi[i]:
            encertats += 1

    # Comptem coincideixen (números que hi són però en altra posició)
    for i in range(4):
        if intent[i] in codi and intent[i] != codi[i]:
            coincideixen += 1

    return encertats, coincideixen

# Programa principal
codi_secret = generar_codi()
print("Benvingut al MasterMind simplificat!")
print("Intenta endevinar el codi de 4 xifres.\n")

endevinat = False

while not endevinat:
    entrada = input("Introdueix un codi de 4 xifres: ")

    # Validació
    if len(entrada) != 4 or not entrada.isdigit():
        print("Error: has d'introduir exactament 4 números!\n")
        continue

    intent = [int(x) for x in entrada]

    encertats, coincideixen = avaluar_intent(codi_secret, intent)

    print(f"Encertats (posició correcta): {encertats}")
    print(f"Coincideixen (número correcte però posició incorrecta): {coincideixen}\n")

    if encertats == 4:
        print(" Has endevinat el codi! Felicitats!")
        endevinat = True