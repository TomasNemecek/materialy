# ---------------------------------------------
#  Řešení – užitečné funkce
# ---------------------------------------------


# 1) Ulož si do proměnné jmeno své jméno a vypiš, kolik má písmen.
jmeno = "Anna"
print(len(jmeno))         # 4


# 2) Vypiš absolutní hodnotu rozdílu čísel 4 a 11.
print(abs(4 - 11))        # 7   z -7 udělá abs kladné číslo


# 3) Máš číslo 2.71828. Zaokrouhli ho na celé číslo a vypiš.
#    Pak ho zaokrouhli na jedno desetinné místo a taky vypiš.
print(round(2.71828))     # 3
print(round(2.71828, 1))  # 2.7


# 4) Máš tři čísla. Vypiš to největší a na dalším řádku to nejmenší.
a = 17
b = 4
c = 23
print(max(a, b, c))       # 23
print(min(a, b, c))       # 4


# 5) Vypiš součet všech čísel od 1 do 10.
print(sum(range(1, 11)))  # 55   pozor: DO se nepočítá, proto 11


# 6) Zeptej se uživatele na dvě čísla a vypiš to větší z nich.
prvni = int(input("Zadej první číslo: "))
druhe = int(input("Zadej druhé číslo: "))
print(max(prvni, druhe))


# 7) Uživatel zadá počet sekund (třeba 3661). Přepočítej ho na hodiny,
#    minuty a sekundy a vypiš je jako 1:1:1 jediným printem.
sekundy = int(input("Zadej počet sekund: "))
hodiny = sekundy // 3600            # kolik celých hodin
minuty = sekundy % 3600 // 60       # ze zbytku kolik celých minut
zbyle = sekundy % 60                # a co zbyde jsou sekundy
print(hodiny, minuty, zbyle, sep=":")   # pro 3661 vypíše 1:1:1


# 8) Zboží stojí 1000 Kč bez DPH. Na jeden řádek vypiš cenu bez DPH
#    i s DPH (21 %). Použij dva printy – první nech řádek pokračovat,
#    druhý ho dokonči.
cena = 1000
print("bez DPH:", cena, "Kč,", end=" ")     # end=" " – řádek pokračuje
print("s DPH:", round(cena * 1.21), "Kč")   # bez DPH: 1000 Kč, s DPH: 1210 Kč


# 9) Zeptej se uživatele na tři čísla (klidně i záporná) a vypiš,
#    jak velké je to největší z nich bez ohledu na znaménko.
#    Např. z čísel -20, 5 a 12 je největší velikost 20.
a = int(input("Zadej první číslo: "))
b = int(input("Zadej druhé číslo: "))
c = int(input("Zadej třetí číslo: "))
print(max(abs(a), abs(b), abs(c)))     # abs zahodí znaménko, max vybere největší
