
class Televizor:
    def __init__(self, marca, diagonala, serie):
        self.marca = marca # publica
        self._diagonala = diagonala # protected(internal)
        self.__serie = serie  # privata

    ## @property  - decorator
    ## Transforma o metoda in atribut
    ## Getter - citeste o valoare/Setter - seteaza o valoare
    @property
    def identificator(self):
        return self.__serie

    


tv1 = Televizor("LG", 138, "23718")
print(tv1.marca)
print(tv1._diagonala)
print(tv1._Televizor__serie) # Desi se pot accesa proprietati private !!!! NU ESTE RECOMANDAT !!!!!

print(tv1.identificator)
print(tv1.identificator)

tv1.marca = "Sony"
tv1._diagonala = 169
tv1._Televizor__serie = "242164782"
print(tv1.marca)
print(tv1._diagonala)
print(tv1._Televizor__serie)  # Desi se pot accesa proprietati private !!!! NU ESTE RECOMANDAT !!!!!



tv1.identificator = "jdhasdaksjh"