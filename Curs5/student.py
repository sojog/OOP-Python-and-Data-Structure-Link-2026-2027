class Student:
    def __init__(self,nume, note: list):
        self.nume = nume
        self.note = note
    
    def __str__(self):
        return f"Studentul {self.nume} are media generala: {self.medie_generala}"
    
    def show_details(self):
        return str(self)
    
    @property    
    def medie_gen(self):
        medie_generala = 0
        for nota in self.note:
            medie_generala += nota
        if len(self.note) > 0:
            return medie_generala/len(self.note)
        
        return 0
    
    def add_grade(self,nota):
        if 0 < nota <= 10:
            self.note.append(nota)
    
    def __iadd__(self,nota):
        if 0 < nota <= 10:
            self.note.append(nota)
        
        return self
            
    def reset_grade(self):
        self.note = []
        return self.note


    def compare_grades(self, other):
        return self.medie_gen > other.medie_gen
    
    # Va fi folosit in obiect1 < obiect2 (gt - greater than)
    def __gt__(self,other):
        return self.medie_gen > other.medie_gen

    # Va fi folosit in obiect1 < obiect2 (lt - less than)
    def __lt__(self,other):
        return self.medie_gen < other.medie_gen

# Variabila specială __name__: Este o variabilă globală pe care interpretorul Python o creează automat pentru fiecare modul.
# Import ca modul: Când alt fișier importă scriptul, Python setează variabila __name__ la numele fișierului
if __name__ == "__main__":

    student1 = Student("Mihai", [10,8,6,9])
    student2 = Student("Andrei", [8,9,7,5])

    print(student1 > student2)
    print(student1.medie_gen)
    student1 += 10
    print(student1.medie_gen)