# ---------------------------------------------
#  Řešení – bonusová cvičení: procházení a kombinace
# ---------------------------------------------


# B1) Trojúhelník z hvězdiček. Uživatel zadá výšku a ty vypiš
#     trojúhelník, kde první řádek má jednu hvězdičku, druhý dvě atd.:
#     *
#     **
#     ***
vyska = int(input("Jak vysoký trojúhelník? "))
for radek in range(1, vyska + 1):
    print("*" * radek)                   # "*" * 3 je "***"


# B2) Rámeček. Uživatel zadá velikost N. Vnořenými cykly nakresli
#     čtverec N x N, kde okraj tvoří X a vnitřek je prázdný. Pro N=4:
#         X X X X
#         X     X
#         X     X
#         X X X X
#     Zamysli se: na kterém řádku a sloupci se kreslí X a kdy mezera?
n = int(input("Jak velký rámeček? "))
for radek in range(n):
    for sloupec in range(n):
        if radek == 0 or radek == n - 1 or sloupec == 0 or sloupec == n - 1:
            print("X", end=" ")
        else:
            print(" ", end=" ")
    print()


# B3) Ciferný součet. Uživatel zadá číslo. Sečti jeho jednotlivé číslice
#     a součet vypiš (třeba z 253 vyjde 2 + 5 + 3 = 10).
cislo = input("Zadej číslo: ")           # necháme jako text, ať projdeme číslice
soucet = 0
for znak in cislo:
    soucet = soucet + int(znak)          # každou číslici převedeme na číslo
print("Ciferný součet:", soucet)


# B4) Teplotní skok. Uživatel postupně zadá sedm denních teplot
#     (klidně i záporných). Najdi a vypiš největší skok mezi dvěma
#     sousedními dny – tedy největší rozdíl teplot ze dne na den
#     (bez ohledu na to, jestli teplota stoupla, nebo klesla).
predchozi = int(input("Zadej teplotu: "))
nejvetsi_skok = 0
for den in range(6):                     # zbývá dalších šest dní
    teplota = int(input("Zadej teplotu: "))
    skok = abs(teplota - predchozi)      # rozdíl proti včerejšku, bez ohledu na směr
    if skok > nejvetsi_skok:
        nejvetsi_skok = skok
    predchozi = teplota                  # dnešek se stane včerejškem
print("Největší skok:", nejvetsi_skok)


# B5) Palindrom. Uživatel zadá slovo. Zjisti, jestli se čte stejně
#     zepředu i zezadu (třeba "kajak" nebo "radar").
#     Zamysli se, jak si slovo poskládáš pozpátku a jak obě verze porovnáš.
slovo = input("Napiš slovo: ")
obracene = ""
for znak in slovo:
    obracene = znak + obracene           # každé písmeno dáme PŘED dosavadní výsledek
if slovo == obracene:
    print("Je to palindrom.")
else:
    print("Není to palindrom.")
