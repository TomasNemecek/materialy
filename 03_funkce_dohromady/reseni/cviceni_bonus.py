# ---------------------------------------------
#  Řešení – bonusová cvičení: funkce dohromady
# ---------------------------------------------
from random import randrange


# B1) Kvíz ze tří otázek.
def otazka(text, spravna_odpoved):
    odpoved = input(text)
    return odpoved == spravna_odpoved


body = 0
if otazka("Hlavní město Česka? ", "Praha"):
    body = body + 1
if otazka("Kolik je 7 * 8? ", "56"):
    body = body + 1
if otazka("Jak se jmenuje cyklus, co běží dokud platí podmínka? ", "while"):
    body = body + 1

print("Skóre:", body, "ze 3")


# B2) Největší ze tří čísel.
def vetsi(a, b):
    if a > b:
        return a
    else:
        return b


def nejvetsi_ze_tri(a, b, c):
    return vetsi(vetsi(a, b), c)


print(nejvetsi_ze_tri(3, 9, 5))


# B3) Hádání čísla poskládané z funkcí.
def vylosuj_cislo():
    return randrange(1, 21)


def zeptej_se_na_tip():
    return int(input("Hádej číslo od 1 do 20: "))


def porovnej(tip, hledane):
    if tip == hledane:
        return True
    if tip > hledane:
        print("Moc velké.")
    else:
        print("Moc malé.")
    return False


hledane_cislo = vylosuj_cislo()
while True:
    tip = zeptej_se_na_tip()
    if porovnej(tip, hledane_cislo):
        print("Trefa!")
        break
