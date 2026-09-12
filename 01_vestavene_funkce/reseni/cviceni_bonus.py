# ---------------------------------------------
#  Řešení – bonusová cvičení: užitečné funkce
# ---------------------------------------------


# B1) Uživatel zadá celkovou cenu útraty a počet lidí. Vypiš, kolik
#     zaplatí každý, zaokrouhleno na dvě desetinná místa.
cena = int(input("Kolik jste utratili? "))
lidi = int(input("Kolik vás bylo? "))
print(round(cena / lidi, 2))        # pro 1000 a 3 vypíše 333.33


# B2) Průměr od 1 do N. Uživatel zadá číslo N. Vypiš průměr všech čísel
#     od 1 do N (součet čísel vyděl jejich počtem).
n = int(input("Zadej N: "))
prumer = sum(range(1, n + 1)) / n       # +1, aby se počítalo i samotné N
print(prumer)                           # pro 10 vypíše 5.5


# B3) Cíl a rozpočet. Uživatel zadá cenu tří položek. Vypiš nejlevnější
#     a nejdražší z nich a jestli se všechny tři vejdou do rozpočtu 1000 Kč.
cena1 = int(input("Cena 1: "))
cena2 = int(input("Cena 2: "))
cena3 = int(input("Cena 3: "))
print("Nejlevnější:", min(cena1, cena2, cena3))
print("Nejdražší:", max(cena1, cena2, cena3))
if cena1 + cena2 + cena3 <= 1000:
    print("Vejdou se do rozpočtu.")
else:
    print("Rozpočet nestačí.")
