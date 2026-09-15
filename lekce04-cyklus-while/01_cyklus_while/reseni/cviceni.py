# ---------------------------------------------
#  Řešení – cyklus while
# ---------------------------------------------


# 1) Odpočítávej cyklem while od 10 do 1 a nakonec vypiš "Start!".
cislo = 10
while cislo >= 1:
    print(cislo)
    cislo = cislo - 1
print("Start!")


# 2) Zdvojnásobuj 1, dokud číslo nepřesáhne 1000.
cislo = 1
kolikrat = 0
while cislo <= 1000:
    cislo = cislo * 2
    kolikrat = kolikrat + 1
print("Číslo:", cislo)
print("Počet zdvojnásobení:", kolikrat)


# 3) Ptej se uživatele "Jaké je hlavní město Česka? " tak dlouho,
#    dokud nenapíše "Praha". Pak vypiš "Správně!".
odpoved = input("Jaké je hlavní město Česka? ")
while odpoved != "Praha":
    odpoved = input("Jaké je hlavní město Česka? ")
print("Správně!")


# 4) Uživatel postupně zadává čísla. Sčítej je. Jakmile zadá 0,
#    přestaň se ptát a vypiš celkový součet.
soucet = 0
cislo = int(input("Zadej číslo (0 = konec): "))
while cislo != 0:
    soucet = soucet + cislo
    cislo = int(input("Zadej číslo (0 = konec): "))
print("Součet je", soucet)


# 5) Pořád dokola se ptej "Napiš slovo: " a to slovo vypiš.
#    Když uživatel napíše "konec", ukonči cyklus příkazem break.
while True:
    slovo = input("Napiš slovo: ")
    if slovo == "konec":
        break
    print(slovo)
print("Konec.")


# 6) Ptej se na heslo. Když uživatel zadá "pyladies", vypiš "Vítej!"
#    a skonči. Když se splete třikrát, vypiš "Zablokováno." a skonči taky.
pokusy = 0
while True:
    heslo = input("Zadej heslo: ")
    pokusy = pokusy + 1
    if heslo == "pyladies":
        print("Vítej!")
        break
    if pokusy == 3:
        print("Zablokováno.")
        break
    print("Špatně, zkus to znovu.")


# 7) Vypisuj zadaná jména, prázdnou odpověď přeskoč pomocí continue.
while True:
    jmeno = input("Jméno: ")
    if jmeno == "konec":
        break
    if jmeno == "":
        continue
    print(jmeno)
print("Konec.")
