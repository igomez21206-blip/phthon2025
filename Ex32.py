def mostrar_majors_que(tupla, limit):
    """Imprimeix tots els valors de la tupla que són majors que 'limit'."""
    for valor in tupla:
        if valor > limit:
            print(valor)

# Programa principal
valors = []

print("Introdueix valors enters per a la tupla (escriu 'fi' per acabar):")

while True:
    entrada = input("Valor: ")
    if entrada.lower() == "fi":
        break
    try:
        valors.append(int(entrada))
    except ValueError:
        print("Si us plau, introdueix un número enter.")

# Convertim la llista a tupla
tupla_valors = tuple(valors)

print("\nValors majors de 18 anys:")
mostrar_majors_que(tupla_valors, 18)