# ---------------------------------------------
#  Řešení – procházení a kombinace
# ---------------------------------------------


# 1) Analýza věty. Uživatel zadá větu. Projdi ji znak po znaku a vypiš
#    počet znaků, počet samohlásek, počet mezer a počet slov ve větě.
#    (Počet slov = počet mezer + 1.)
veta = input("Napiš větu: ")
samohlasky = 0
mezery = 0
for znak in veta:
    if znak in "aeiou":
        samohlasky = samohlasky + 1
    if znak == " ":
        mezery = mezery + 1
print("Počet znaků:", len(veta))
print("Samohlásek:", samohlasky)
print("Mezer:", mezery)
print("Slov:", mezery + 1)              # slov je o jedno víc než mezer


# 2) Bum-Bác. Tuhle úlohu znáš z minula pro jedno číslo – teď ji necháme
#    proběhnout cyklem. Vypiš čísla od 1 do 30, ale:
#    - za dělitelné třemi i pěti zároveň vypiš "BumBác",
#    - za dělitelné jen třemi vypiš "Bum",
#    - za dělitelné jen pěti vypiš "Bác",
#    - jinak vypiš samotné číslo.
for cislo in range(1, 31):
    if cislo % 15 == 0:                 # dělitelné 3 i 5 = dělitelné 15, musí být první
        print("BumBác")
    elif cislo % 3 == 0:
        print("Bum")
    elif cislo % 5 == 0:
        print("Bác")
    else:
        print(cislo)


# 3) Statistika čísel. Uživatel zadá, kolik čísel bude zadávat, a pak
#    ta čísla postupně napíše. V jednom průchodu cyklem spočítej a vypiš
#    jejich součet, průměr, největší a nejmenší číslo.
#    Nepoužívej funkce sum, max ani min – spočítej vše sama cyklem.
pocet = int(input("Kolik čísel zadáš? "))
prvni = int(input("Zadej číslo: "))
soucet = prvni
nejvetsi = prvni                        # první číslo je zatím největší i nejmenší
nejmensi = prvni
for i in range(pocet - 1):              # první už máme, zbývá o jedno míň
    cislo = int(input("Zadej číslo: "))
    soucet = soucet + cislo
    if cislo > nejvetsi:
        nejvetsi = cislo
    if cislo < nejmensi:
        nejmensi = cislo
print("Součet:", soucet)
print("Průměr:", soucet / pocet)
print("Největší:", nejvetsi)
print("Nejmenší:", nejmensi)


# 4) Násobilková tabulka. Pomocí vnořených cyklů vypiš tabulku 4x4,
#    kde na řádku R a sloupci S je jejich součin:
#        1 2 3 4
#        2 4 6 8
#        3 6 9 12
#        4 8 12 16
#    Jak pojmenuješ obě proměnné cyklu? Zamysli se, ať dávají smysl.
for radek in range(1, 5):
    for sloupec in range(1, 5):
        print(radek * sloupec, end=" ")
    print()                             # po každém řádku skoč na nový řádek


# 5) Hody dvěma kostkami. Vnořenými cykly vypiš všechny možné hody
#    dvěma kostkami (každá má čísla 1 až 6) a u každého i jejich součet.
#    Každý řádek bude vypadat třeba takhle: 2 + 5 = 7
for kostka1 in range(1, 7):
    for kostka2 in range(1, 7):
        print(kostka1, "+", kostka2, "=", kostka1 + kostka2)
