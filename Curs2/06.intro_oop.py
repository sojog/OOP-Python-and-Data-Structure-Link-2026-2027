# Conventie - functiile incep cu litere mici
# Conventie - clasele incep cu litere mare

# Definirea unei clase (sablon)
class Animal:
    # functie (metoda) initiliazatoare (constructor)
    def __init__(self, nume):
        self.nume = nume

      
obiect_de_tip_animal = Animal("Thomas")
print(obiect_de_tip_animal, "are numele:", obiect_de_tip_animal.nume)


alt_obiect_de_tip_animal = Animal("Jerry")
print(alt_obiect_de_tip_animal, "are numele:", alt_obiect_de_tip_animal.nume)

un_cu_totul_alt_obiect_de_tip_animal = Animal("Spike")
print(un_cu_totul_alt_obiect_de_tip_animal, "are numele:", un_cu_totul_alt_obiect_de_tip_animal.nume)