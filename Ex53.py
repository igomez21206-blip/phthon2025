def index_paraula(llista, paraula):
    esquerra = 0
    dreta = len(llista) - 1

    while esquerra <= dreta:
        mig = (esquerra + dreta) // 2
        if llista[mig] == paraula:
            return mig
        elif llista[mig] < paraula:
            esquerra = mig + 1
        else:
            dreta = mig - 1

    return -1
