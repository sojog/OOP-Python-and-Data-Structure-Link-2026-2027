traduceri = {
    "ro" : "Salut",
    "en" : "Hello",
    "de" : "Hallo",
    "it" : "Ciao",
    "es" : "Ola",
    "fr" : "Bonjour",
}


def localizare(limba, nume):
    if salut := traduceri.get(limba):
        return f"{salut} {nume}" # La return functia nu mai continua
    return f"Limba necunoscuta, {nume}"


print(localizare("ro", "Ion"))
print(localizare("en", "John"))
print(localizare("us", "John"))