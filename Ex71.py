def llegir_fitxer(nom_fitxer):
    """
    Llegeix el contingut d'un fitxer.
    Controla que el fitxer existeixi i gestiona errors d'obertura.
    """
    try:
        with open(nom_fitxer, 'r', encoding='utf-8') as fitxer:
            contingut = fitxer.read()
        return contingut
    except FileNotFoundError:
        print(f"Error: El fitxer '{nom_fitxer}' no existeix.")
        return None
    except IOError:
        print(f"Error: No s'ha pogut llegir el fitxer '{nom_fitxer}'.")
        return None
