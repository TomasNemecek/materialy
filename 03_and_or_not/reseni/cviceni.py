# ---------------------------------------------
#  Řešení – and / or / not
# ---------------------------------------------


# 1) Platný trojúhelník. Ze tří stran jde sestavit trojúhelník jen tehdy,
#    když je součet každých dvou stran větší než ta třetí.
#    Vypiš "Platný trojúhelník." / "Takový trojúhelník nejde.".
a = 3
b = 4
c = 5
if a + b > c and a + c > b and b + c > a:
    print("Platný trojúhelník.")
else:
    print("Takový trojúhelník nejde.")


# 2) Přestupný rok. Rok je přestupný, když je dělitelný čtyřmi,
#    ale ne stovkou – NEBO když je dělitelný čtyřmi sty.
#    Zeptej se na rok a vypiš "Přestupný." / "Nepřestupný.".
#    (Vyzkoušej 2024, 1900, 2000.)
rok = int(input("Zadej rok: "))
if (rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0:
    print("Přestupný.")
else:
    print("Nepřestupný.")


# 3) Přihlášení. Správné jméno je "anna" a správné heslo je "tajne".
#    Zeptej se na jméno i heslo a vypiš "Vítej!", jen když sedí obojí.
#    Jinak vypiš "Špatné údaje.".
jmeno = input("Jméno: ")
heslo = input("Heslo: ")
if jmeno == "anna" and heslo == "tajne":
    print("Vítej!")
else:
    print("Špatné údaje.")


# 4) Smíš řídit? Řídit můžeš, jen když máš řidičák a zároveň
#    zrovna NEMÁŠ zákaz řízení. Vypiš "Můžeš řídit." / "Za volant nesmíš.".
ma_ridicak = True
ma_zakaz = True
if ma_ridicak and not ma_zakaz:
    print("Můžeš řídit.")
else:
    print("Za volant nesmíš.")


# 5) Sleva na vstupné. Slevu mají děti (do 18 let) a senioři (65 a víc).
#    Navíc mají v pondělí slevu úplně všichni.
#    Zeptej se na věk a na den a vypiš "Máš slevu." / "Plné vstupné.".
vek = int(input("Věk: "))
den = input("Den: ")
if vek < 18 or vek >= 65 or den == "pondělí":
    print("Máš slevu.")
else:
    print("Plné vstupné.")


# 6) Zabezpečení domu. Dům je zabezpečený, jen když jsou zavřené dveře,
#    zavřená okna a zároveň zapnutý alarm.
#    Zeptej se na všechny tři věci (ano/ne). Pomocí not (…) vypiš
#    "Pozor, dům není zabezpečený!", když zabezpečený NENÍ,
#    jinak vypiš "Zabezpečeno.".
dvere = input("Zavřené dveře? (ano/ne) ")
okna = input("Zavřená okna? (ano/ne) ")
alarm = input("Zapnutý alarm? (ano/ne) ")
if not (dvere == "ano" and okna == "ano" and alarm == "ano"):
    print("Pozor, dům není zabezpečený!")
else:
    print("Zabezpečeno.")
