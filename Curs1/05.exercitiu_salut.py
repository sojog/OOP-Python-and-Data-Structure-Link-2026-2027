salutari = {
    "ro" : "Salut",
    "en" : "Hello",
    "de" : "Hallo",
    "it" : "Ciao",
    "es" : "Ola",
    "fr" : "Bonjour",
}


while True:
    limba = input("Introdu limba dorita \n")
    print(salutari.get(limba, "necunoscuta"))