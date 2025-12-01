def es_palindrom(paraula):
    paraula = paraula.lower()  # Convertim a minúscules per evitar diferències
    return paraula == paraula[::-1]
