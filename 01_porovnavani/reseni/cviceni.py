# ---------------------------------------------
#  Řešení – porovnávání a booleovské hodnoty
# ---------------------------------------------


# 1) Máš proměnnou cena. Vypiš True/False podle toho,
#    jestli je cena menší nebo rovna 50.
cena = 65
print(cena <= 50)     # False, cena je 65


# 2) Vypiš True/False podle toho, jestli je číslo 12 dělitelné třemi.
print(12 % 3 == 0)    # True, zbytek po dělení je 0


# 3) Ulož do proměnné vysledek porovnání, jestli je 2 + 2 rovno 4.
#    Pak proměnnou vysledek vypiš.
vysledek = 2 + 2 == 4
print(vysledek)       # True


# 4) Studentka má tři známky. Spočítej jejich průměr do proměnné prumer
#    a vypiš True/False podle toho, jestli má na vyznamenání
#    (průměr menší nebo rovný 2).
znamka1 = 1
znamka2 = 3
znamka3 = 2
prumer = (znamka1 + znamka2 + znamka3) / 3
print(prumer <= 2)    # True, průměr je 2.0


# 5) Zeptej se uživatele na číslo a vypiš True/False podle toho,
#    jestli je větší než 100.
cislo = int(input("Zadej číslo: "))
print(cislo > 100)


# 6) Vypiš True/False podle toho, jestli je 2 na desátou (2 ** 10)
#    větší než tisíc.
print(2 ** 10 > 1000)     # True – 2 ** 10 je 1024, těsně nad tisíc
