class Televizor:
    
    def __init__(self, marca, diagonala, serie):
        self.marca = marca # publica
        self._diagonala = diagonala # protected(internal)
        self.__serie = serie  # privata
        self.__memorie = 100

    ## @property  - decorator
    ## Transforma o metoda in atribut
    ## Getter - citeste o valoare/Setter - seteaza o valoare
    @property
    def identificator(self):
        return self.__serie

    @property
    def memorie(self):
        return self.__memorie

    @memorie.setter
    def memorie(self, o_noua_valoare):
        if isinstance(o_noua_valoare, int) and o_noua_valoare > 100:
            self.__memorie = o_noua_valoare


tv1 = Televizor("LG", 138, "23718")
print(tv1.identificator)
print(tv1.memorie)

tv1.memorie = 200
print(tv1.memorie)


tv1.memorie = [49832,32]
print(tv1.memorie)