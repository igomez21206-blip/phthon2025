# Definim la funció
def comptar_majuscules(cadena):
    comptador = 0
    for lletra in cadena:
        if lletra.isupper():  # isupper() retorna True si la lletra és majúscula
            comptador += 1
    return comptador