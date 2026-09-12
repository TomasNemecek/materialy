# ---------------------------------------------
#  Vzorové řešení: bonusová cvičení input
# ---------------------------------------------
# Tvoje řešení může vypadat trochu jinak, a to je v pořádku.


# B1) Zeptej se uživatele na dvě čísla a vypiš jejich součet.
a = int(input("Zadej první číslo: "))
b = int(input("Zadej druhé číslo: "))
print("Součet je", a + b)


# B2) Zeptej se na částku a na počet lidí.
#     Vypiš, kolik zaplatí každý a kolik korun zbyde.
castka = int(input("Kolik je účet? "))
lidi = int(input("Kolik vás je? "))
print("Každý zaplatí:", castka // lidi)
print("Zbyde:", castka % lidi)


# B3) Zeptej se na jméno a na číslo.
#     Vypiš jméno tolikrát za sebou.
jmeno = input("Jak se jmenuješ? ")
pocet = int(input("Kolikrát? "))
print(jmeno * pocet)
