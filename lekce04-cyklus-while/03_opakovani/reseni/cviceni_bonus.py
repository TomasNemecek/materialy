# ---------------------------------------------
#  Řešení – bonusová cvičení: opakování
# ---------------------------------------------
from random import randrange


# B1) Hra "kámen, nůžky, papír".
while True:
    tvuj_tah = input("Tvůj tah (kamen/nuzky/papir): ")

    # Počítač umí vylosovat jen číslo, tak si ho přeložíme na tah.
    cislo = randrange(1, 4)
    if cislo == 1:
        pocitac = "kamen"
    elif cislo == 2:
        pocitac = "nuzky"
    else:
        pocitac = "papir"
    print("Počítač hrál:", pocitac)

    # Kdo vyhrál: kámen tupí nůžky, nůžky stříhají papír, papír balí kámen.
    vyhrala_kamenem = tvuj_tah == "kamen" and pocitac == "nuzky"
    vyhrala_nuzkami = tvuj_tah == "nuzky" and pocitac == "papir"
    vyhrala_papirem = tvuj_tah == "papir" and pocitac == "kamen"

    if tvuj_tah == pocitac:
        print("Remíza.")
    elif vyhrala_kamenem or vyhrala_nuzkami or vyhrala_papirem:
        print("Vyhrála jsi!")
    else:
        print("Prohrála jsi.")

    znovu = input("Hrát znovu? (ano/ne) ")
    if znovu == "ne":
        break

print("Díky za hru!")


# B2) Trojúhelník z hvězdiček, vysoký N.
n = int(input("Zadej N: "))
for radek in range(1, n + 1):
    print("*" * radek)


# B3) Součet číslic zadaného čísla.
#     Postupně utrháváme poslední číslici, dokud něco zbývá.
cislo = int(input("Zadej celé číslo: "))
cislo = abs(cislo)                   # u záporného čísla zahodíme minus
soucet = 0
while cislo > 0:
    soucet = soucet + cislo % 10     # poslední číslice
    cislo = cislo // 10              # utrhneme ji
print("Součet číslic je", soucet)
