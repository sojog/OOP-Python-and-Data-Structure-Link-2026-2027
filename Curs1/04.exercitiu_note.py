note = {
    "1" : "insuficient",
    "2" : "suciecient",
    "3" : "bine",
    "4" : "foarte bine",
    "5" : "excelent"
}


# print("41" in note)
nota = input("Introdu nota pt a lua calificativul\n")

# Versiunea 1
# if nota in note:
#     print("Ai luat:",note[nota])
# else:
#     print("Nota nu este corecta")

# Versiunea 2
print(note.get(nota, "Nota nu este corecta"))
