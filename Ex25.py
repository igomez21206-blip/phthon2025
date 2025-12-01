def crear_punts(n=10, max_x=200, max_y=200):
    punts = []
    for _ in range(n):
        x = random.randint(-max_x, max_x)
        y = random.randint(-max_y, max_y)
        punts.append((x, y))
    return punts