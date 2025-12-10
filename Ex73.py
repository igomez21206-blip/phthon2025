from abc import ABC, abstractmethod

# Classe base
class Animal(ABC):
    def __init__(self, especie, edat):
        self.especie = especie
        self.edat = edat

    @abstractmethod
    def xerrar(self): pass

    @abstractmethod
    def mourem(self): pass

    def quisoc(self):
        print(f"{self.especie} està al quisoc.")

# Subclasses
class Cavall(Animal):
    def xerrar(self): print("Neigh!")
    def mourem(self): print("El cavall corre pel prat.")

class Dofí(Animal):
    def xerrar(self): print("Click-click!")
    def mourem(self): print("El dofí neda a la mar.")

class Abella(Animal):
    def xerrar(self): print("Bzzzz!")
    def mourem(self): print("L'abella vola.")
    def picar(self): print("L'abella pica!")

class Humà(Animal):
    def __init__(self, especie, edat, nom):
        super().__init__(especie, edat)
        self.nom = nom
    def xerrar(self): print(f"{self.nom} diu hola!")
    def mourem(self): print(f"{self.nom} camina.")

class Fiet(Humà):
    def __init__(self, especie, edat, nom, pares):
        super().__init__(especie, edat, nom)
        self.pares = pares
    def nompares(self): print(f"Els pares de {self.nom} són: {', '.join(self.pares)}")

class Centaure(Cavall, Humà):
    def __init__(self, especie, edat, nom):
        Cavall.__init__(self, especie, edat)
        self.nom = nom
    def xerrar(self): print(f"{self.nom} diu amb veu humana i neigheja!")
    def mourem(self): print(f"{self.nom} galopa i camina.")

# Classe independent
class Xou:
    def xerrar(self): print("Xou fa un soroll espectacular!")
    def mourem(self): print("Xou es mou elegantment.")
    def quisoc(self): print("Xou està al seu propi quisoc.")

# Llista d'elements
elements = [
    Cavall("Cavall", 5),
    Dofí("Dofí", 8),
    Abella("Abella", 1),
    Humà("Humà", 30, "Joan"),
    Fiet("Humà", 5, "Marta", ["Anna", "Pere"]),
    Centaure("Centaure", 200, "Centa"),
    Xou()
]

# Bucle per cridar mètodes comuns i específics
for e in elements:
    print(f"\nElement: {type(e).__name__}")
    e.xerrar()
    e.mourem()
    e.quisoc()
    if isinstance(e, Abella): e.picar()
    if isinstance(e, Fiet): e.nompares()