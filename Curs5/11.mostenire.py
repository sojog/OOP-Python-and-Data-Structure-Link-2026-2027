
class Animal:
    def __init__(self, varsta, greutate):
        self.varsta = varsta
        self.greutate = greutate

    def __str__(self):
        return f"Animalul are {self.varsta} ani si {self.greutate} kg"

    def o_alta_metoda(self):
        return "????"

# mostenire
class Pisica(Animal):
    def miauna(self):
        return "Miau miau miau"

class PisicaBirmaneza(Pisica):
    pass

# suprascriere (overwriting)
class PisicaSiameza(Pisica):
    def miauna(self):
        return "Mbbbbiau mbbbiau mbbbiau"



animal1= Animal(2, 45)
print(animal1)

pisica1 = Pisica(20, 8)
print(pisica1)

print(pisica1.o_alta_metoda())

print(pisica1.miauna())


pisica_birm =  PisicaBirmaneza(20, 8)
print(pisica_birm.miauna())

pisica_siam =  PisicaSiameza(20, 8)
print(pisica_siam.miauna())