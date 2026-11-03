# Conventie - functiile incep cu litere mici
# Conventie - clasele incep cu litere mare

# Definirea unei clase (sablon)
class Animal:

    # functie (metoda) initiliazatoare (constructor)
    def __init__(self, nume, varsta):
        # atribut (variabila)
        self.nume = nume
        self.varsta = varsta

    def este_batran(self):
        return self.varsta > 4

      
obiect1 = Animal("Thomas", 5)
print(obiect1, "are numele:", obiect1.nume, "are varsta:", obiect1.varsta)
print(obiect1.nume, "este batran:", obiect1.este_batran())


obiect2 = Animal("Jerry", 2)
print(obiect2, "are numele:", obiect2.nume, "are varsta:", obiect2.varsta)
print(obiect2.nume, "este batran:", obiect2.este_batran())

obiect3 = Animal("Spike", 7)
print(obiect3, "are numele:", obiect3.nume, "are varsta:", obiect3.varsta)
print(obiect3.nume, "este batran:", obiect3.este_batran())