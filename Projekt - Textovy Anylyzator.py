'''
author = VOJTĚCH ŠPAČEK
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

predel = 40 * "-"

#REGISTRACE
registrovani_uzivatele = {
    "bob" : "123",
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass123"
}

jmeno = input("Username: ")
heslo = input("Password: ")

print(predel)

if registrovani_uzivatele.get(jmeno) == heslo:
    print(f"Welcome to the app, {jmeno}!")
    print("We have 3 texts to be analyzed.")

else:
    print("unregistered user, terminating the program..")
    quit()

print(predel)

#ZVOLENÍ TEXTU

cislo_textu = int(input("Enter a number btw. 1 and 3 to select: "))

if cislo_textu > 3:
    print("The entered number is not available, terminating..")
    quit()

if cislo_textu < 1:
    print("The entered number is not available, terminating..")
    quit()

TEXT = TEXTS[cislo_textu - 1]
print(predel)

#POCET SLOV

vycisteny_text = []
pocet_slov = 0
for slovo in TEXT.split():
    vycisteny_text.append(slovo.strip(".:;,"))

for slovo in vycisteny_text:
    pocet_slov +=1

print(f"There are {pocet_slov} words in the selected text.")

#VELKÁ PÍSMENA NA ZAČÁTKU
velka_pismena = 0

for slovo in vycisteny_text:
    if slovo[0].isupper():
        velka_pismena += 1

print(f"There are {velka_pismena} titlecase words.")

#VELKÁ PÍSMENA CELEK
velka_pismena_cele = 0

for slovo  in vycisteny_text:
    if slovo.isalpha() and slovo.isupper():
        velka_pismena_cele += 1

print(f"There are {velka_pismena_cele} uppercase words.")

#MALÁ PÍSMENA
mala_pismena = 0

for slovo in vycisteny_text:
    if slovo.islower():
        mala_pismena +=1

print(f"There are {mala_pismena} lowercase words.")

#ČÍSLA
cisla = 0
soucet = 0
for slovo in vycisteny_text:
    if slovo.isnumeric():
        cisla += 1
        soucet += int(slovo)
print(f"There are {cisla} numeric strings.")

#SOUČET VŠECH ČÍSEL


print(f"The sum of all the numbers {soucet}")

#DÉLKY SLOV
print(f"{predel}\nLEN|  OCCURENCES  |NR.\n{predel}")

delky_slov = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0}

for slovo in vycisteny_text:
    pocet_pismen = 0
    for pismeno in slovo:
        pocet_pismen += 1
    delky_slov[pocet_pismen] += 1


for cislo in delky_slov:
    mezivypocet = delky_slov[cislo]
    hvezdicky = mezivypocet * "*"
    print(
        f"{cislo: >3}|{hvezdicky: <14}|{mezivypocet}"
    )