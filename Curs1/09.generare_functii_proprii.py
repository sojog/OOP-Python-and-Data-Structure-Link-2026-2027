# Intotdeauna functia este definita si apoi folosita

# Definirea unei functii ( def - este cuvant cheie)
def nume_functie ():
    ### Corpul functiei
    pass


# Folosirea functiei
nume_functie ()



# # Functia poate primi parametri
def alt_nume_de_functie(x, y):
    print("Ai introdus", x, y)

alt_nume_de_functie(10, 30)
alt_nume_de_functie(20, "negru")
alt_nume_de_functie("523523", "mouse")


# # Functia este menita sa calculeze ceva si posibil sa intoarca un rezultat

def adunare(x, y):
    return x + y # Return este un cuvant cheie


print(adunare(10, 20))
print(adunare("rosu", "verde"))
print(adunare(-123, 100))


# Type hint
def scadere(x: int , y:int) -> int:
    return x - y # Return este un cuvant cheie

print(scadere(10, 20))
print(scadere(10.23, 1.23))