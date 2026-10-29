def note_catre_calificativ(nota):
    
    note = {
        "1" : "insuficient",
        "2" : "suciecient",
        "3" : "bine",
        "4" : "foarte bine",
        "5" : "excelent"
    }
    return note.get(nota, "Nota nu este corecta")


print(note_catre_calificativ("1"))
print(note_catre_calificativ("5"))