def crear_llista_fitxer(nom_fitxer):
    llista = []
    with open(nom_fitxer, "r", encoding="utf-8") as f:
        for linia in f:
            paraules = linia.split()
            llista.extend(paraules)
    return llista