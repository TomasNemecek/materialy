# ---------------------------------------------
#  Řešení – bonusová cvičení: cyklus while
# ---------------------------------------------
from random import randrange


# B1) Hra "Oko bere".
soucet = 0
while soucet < 21:
    print("Máš", soucet, "bodů.")
    odpoved = input("Chceš si líznout? (ano/ne) ")
    if odpoved == "ne":
        break
    karta = randrange(2, 11)
    print("Lízla sis", karta)
    soucet = soucet + karta

if soucet == 21:
    print("Přesně 21, vyhráváš!")
elif soucet > 21:
    print("Přetáhla jsi přes 21, prohráváš. Máš", soucet)
else:
    print("Končíš s", soucet, "body.")
