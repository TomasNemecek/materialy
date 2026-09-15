# ---------------------------------------------
#  Řešení – opakování
# ---------------------------------------------
from random import randrange


# 1) Čísla od 1 do 30 dělitelná třemi nebo pěti.
for cislo in range(1, 31):
    if cislo % 3 == 0 or cislo % 5 == 0:
        print(cislo)


# 2) Kolikrát je ve slově písmeno "a".
slovo = input("Zadej slovo: ")
pocet = 0
for pismeno in slovo:
    if pismeno == "a":
        pocet = pocet + 1
print("Písmeno 'a' je ve slově", pocet, "krát")


# 3) Součet, počet a průměr zadaných čísel (0 = konec).
soucet = 0
pocet = 0
cislo = int(input("Zadej číslo (0 = konec): "))
while cislo != 0:
    soucet = soucet + cislo
    pocet = pocet + 1
    cislo = int(input("Zadej číslo (0 = konec): "))

if pocet == 0:
    print("Nezadala jsi žádné číslo.")
else:
    print("Součet:", soucet)
    print("Počet:", pocet)
    print("Průměr:", round(soucet / pocet, 1))


# 4) Nejvyšší naměřená teplota.
#    První teplotu si rovnou zapamatujeme jako zatím nejvyšší,
#    každou další s ní porovnáme.
nejvyssi = int(input("Zadej teplotu: "))
while True:
    dalsi = input("Další? (ano/ne) ")
    if dalsi == "ne":
        break
    teplota = int(input("Zadej teplotu: "))
    if teplota > nejvyssi:
        nejvyssi = teplota

print("Nejvyšší teplota byla", nejvyssi)


# 5) Hra "hádej číslo" – pět pokusů.
hadane_cislo = randrange(1, 21)
pokusy = 0
while True:
    odpoved = int(input("Hádej číslo od 1 do 20: "))
    pokusy = pokusy + 1

    if odpoved == hadane_cislo:
        print("Trefa!")
        break

    if pokusy == 5:
        print("Pět pokusů je pryč. Číslo bylo", hadane_cislo)
        break

    if odpoved > hadane_cislo:
        print("Moc velké.")
    else:
        print("Moc malé.")
