# ---------------------------------------------
#  Řešení – bonus (and / or / not)
# ---------------------------------------------


# B1) Druh trojúhelníku. Máš tři strany. Urči a vypiš, jaký to je
#     trojúhelník:
#       - "rovnostranný", když jsou všechny tři strany stejné,
#       - "rovnoramenný", když jsou aspoň dvě strany stejné,
#       - "různostranný", když jsou všechny strany různé.
a = 5
b = 5
c = 8
if a == b and b == c:
    print("rovnostranný")
elif a == b or b == c or a == c:
    print("rovnoramenný")
else:
    print("různostranný")


# B2) Vstup do klubu. Dovnitř smí ten, komu je aspoň 18 let A ZÁROVEŇ
#     je buď členem, NEBO má pozvánku.
#     Kdo má zákaz vstupu, dovnitř nesmí nikdy – ani člen, ani s pozvánkou.
#     Zamysli se, kam patří závorky, aby podmínka fungovala správně.
#     Vypiš "Vítej v klubu." / "Dnes se nedostaneš.".
vek = 20
je_clen = False
ma_pozvanku = True
ma_zakaz = True

if not ma_zakaz and vek >= 18 and (je_clen or ma_pozvanku):
    print("Vítej v klubu.")
else:
    print("Dnes se nedostaneš.")


# B3) Kámen, nůžky, papír. Zeptej se obou hráčů na tah – ať zadají
#     "kamen", "nuzky" nebo "papir". Vypiš, kdo vyhrál:
#       - "Remíza.", když mají oba stejně,
#       - jinak urči vítěze podle pravidel:
#           kámen tupí nůžky, nůžky stříhají papír, papír balí kámen.
#     Vypiš "Vyhrál hráč 1." / "Vyhrál hráč 2.".
hrac1 = input("Hráč 1 (kamen/nuzky/papir): ")
hrac2 = input("Hráč 2 (kamen/nuzky/papir): ")
if hrac1 == hrac2:
    print("Remíza.")
elif (hrac1 == "kamen" and hrac2 == "nuzky") or (hrac1 == "nuzky" and hrac2 == "papir") or (hrac1 == "papir" and hrac2 == "kamen"):
    print("Vyhrál hráč 1.")
else:
    print("Vyhrál hráč 2.")
