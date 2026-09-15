# ---------------------------------------------
#  Řešení – for vs while
# ---------------------------------------------


# ---------------------------------------------
#  Část 1 – jaký cyklus by se hodil?
# ---------------------------------------------
# 1)  for   – hřebíků je deset, počet známe předem.
# 2)  while – kolik ran bude potřeba, dopředu nevíme.
# 3)  while – jak dlouho se voda bude vařit, dopředu nevíme.
# 4)  while – panna může padnout hned, nebo až po deseti hodech.
# 5)  while – šestky počítáme, ale kolik hodů na tři bude potřeba nevíme.
# 6)  for   – jakmile uživatelka číslo zadá, počet opakování známe.
# 7)  žádný cyklus – hodíme jednou a vypíšeme, nic se neopakuje.
# 8)  for   – čísla od 0 do 100 jsou daná, range(0, 101, 2).
# 9)  for   – počet je daný zadaným číslem, jen ho neznáme při psaní kódu.
# 10) for   – procházíme text, počet písmen je daný.
# 11) while – kolik jablek se do dvou kilo vejde, dopředu nevíme.
# 12) for   – odpovědí je třicet.


# ---------------------------------------------
#  Část 2 – kód
# ---------------------------------------------


# 1) Vypiš všechna písmena slova "Python", každé na svůj řádek.
#    Počet opakování známe (kolik má slovo písmen) -> for.
for pismeno in "Python":
    print(pismeno)


# 2) Ptej se na PIN tak dlouho, dokud uživatel nezadá "1234".
#    Kolikrát se splete dopředu nevíme -> while.
pin = input("Zadej PIN: ")
while pin != "1234":
    print("Špatný PIN.")
    pin = input("Zadej PIN: ")
print("Odemčeno!")


# 3) Vypiš prvních deset násobků čísla 3 (3, 6, 9, ... 30).
#    Deset opakování, počet známe -> for.
for cislo in range(3, 31, 3):
    print(cislo)

# Jde to i bez kroku – vynásobit si to v cyklu sama:
for cislo in range(1, 11):
    print(cislo * 3)


# 4) Načítej od uživatele čísla tak dlouho, dokud nezadá záporné číslo.
#    Pak vypiš, kolik čísel stihl zadat.
#    Kolik čísel zadá dopředu nevíme -> while.
kolik = 0
cislo = int(input("Zadej číslo: "))
while cislo >= 0:
    kolik = kolik + 1
    cislo = int(input("Zadej číslo: "))
print("Počet zadaných čísel před tím záporným:", kolik)


# 5) V nádrži je 45 litrů, každou minutu uteče 3 litry. Po každé minutě
#    vypiš zbytek, nakonec počet minut.
#    Kolikrát se cyklus zopakuje dopředu nevíme -> while.
voda = 45
minuty = 0
while voda > 0:
    voda = voda - 3
    minuty = minuty + 1
    print("Po", minuty, "minutách zbývá", voda, "litrů.")
print("Nádrž je prázdná po", minuty, "minutách.")
