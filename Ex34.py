def nums_que_comencen_per(noms):
    lletra = input("Introdueix una lletra: ").lower()
    comptador = 0

    for nom in noms:
        if nom.lower().startswith(lletra):
            comptador += 1

    return comptador