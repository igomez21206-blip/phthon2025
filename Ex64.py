def concatenar_llistes(llista1, llista2, connector):
    """
    Concatena els elements de dues llistes amb un connector.
    """
    return [a + connector + b for a, b in zip(llista1, llista2)]

# Exemple de prova
llista1 = ['sub', 'supra']
llista2 = ['campió', 'campiona']
connector = '-'

resultat = concatenar_llistes(llista1, llista2, connector)
print(resultat)