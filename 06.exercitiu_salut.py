salutari = {
    "ro" : "Salut",
    "en" : "Hello",
    "de" : "Hallo",
    "it" : "Ciao",
    "es" : "Ola",
    "fr" : "Bonjour",
}

# limba = input("Introdu limba dorita \n")
# bool(limba)

# Walrus Operator
while limba := input("Introdu limba dorita \n"):
    print(salutari.get(limba, "necunoscuta"))