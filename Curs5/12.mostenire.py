
# Mostenire - Animal se mai numeste clasa de baza / clasa parinte 
class Animal:
    def __init__(self, varsta, greutate):
        if varsta not in range(200):
            raise ValueError("Varsta nu este intreg pana la 200")
        else:
            self.varsta = varsta
      
        self.greutate = greutate

    def __str__(self):
        return f"Animalul are {self.varsta} ani si {self.greutate} kg"

# Caine - este clasa derivata / clasa copil
class Pisica(Animal):
    pass


# Caine - este clasa derivata / clasa copil
class Caine(Animal):
    # Am suprascris __init__
    def __init__(self, varsta, greutate, nume):
        super().__init__(varsta, greutate)
        self.nume = nume

    def __str__(self):
        return  super().__str__() + f" si se numeste {self.nume}"

tom = Pisica(10, 15)
print(tom)

rex = Caine(20, 15, "Rex")
print(rex)
