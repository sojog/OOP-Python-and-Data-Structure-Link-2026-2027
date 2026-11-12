# Mai multi studenti = CLASA

class Student:
    def __init__(self,nume, note: list):
        self.nume = nume
        self.note = note

    @property    
    def medie_gen(self):
        if not self.note: return 0
        medie_generala = 0
        for nota in self.note:
            medie_generala += nota
        return medie_generala/len(self.note)
       
    def __iadd__(self,nota):
        if 0 < nota <= 10:
            self.note.append(nota)
        
        return self

class GrupaStudenti:
    def __init__(self, nume, studenti:list[Student]):
        self.nume = nume
        self.studenti = studenti

    @property    
    def medie_gen(self):
        if not self.studenti: return 0
        medie_generala = 0
        for student in self.studenti:
            medie_generala += student.medie_gen
        return medie_generala/len(self.studenti)


if __name__ == "__main__":
    alin = Student("Alin", [10, 5, 6, 7, 8])
    print("Alin are media", alin.medie_gen)
    
    maria = Student("Maria", [6, 7, 9, 10])
    print("maria are media", maria.medie_gen)

    grupa_A = GrupaStudenti("A", [alin, maria])
    print("Grupa are media", grupa_A.medie_gen)