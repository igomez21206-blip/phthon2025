def comptar_vocals(paraula):
    vocals = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    paraula = paraula.lower()

    for lletra in paraula:
        if lletra in vocals:
            vocals[lletra] += 1

    print(f"Hi ha {vocals['a']} a’s, {vocals['e']} e’s, {vocals['i']} i’s, {vocals['o']} o’s i {vocals['u']} u’s.")