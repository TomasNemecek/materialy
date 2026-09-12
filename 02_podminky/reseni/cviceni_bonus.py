# ---------------------------------------------
#  Řešení – bonus (podmínky)
# ---------------------------------------------


# B1) Sudé, nebo liché?
cislo = int(input("Zadej celé číslo: "))
if cislo % 2 == 0:
    print("Sudé")
else:
    print("Liché")


# B2) Největší ze tří.
#     Zatím bez and/or – poradíme si vnořenými if.
a = 12
b = 25
c = 8
if a >= b:
    if a >= c:
        print(a)
    else:
        print(c)
else:
    if b >= c:
        print(b)
    else:
        print(c)


# B3) Bum-Bác pro jedno číslo.
#     Dělitelnost třemi i pěti = dělitelnost patnácti. Musí se testovat
#     jako první – jinak by číslo spadlo hned do větve "Bum" nebo "Bác"
#     a na "BumBác" by nikdy nedošlo.
cislo = int(input("Zadej číslo: "))
if cislo % 15 == 0:
    print("BumBác")
elif cislo % 3 == 0:
    print("Bum")
elif cislo % 5 == 0:
    print("Bác")
else:
    print(cislo)


# B4) Malá kalkulačka.
a = float(input("První číslo: "))
b = float(input("Druhé číslo: "))
znamenko = input("Znaménko (+, -, *, /): ")

if znamenko == "+":
    print(a + b)
elif znamenko == "-":
    print(a - b)
elif znamenko == "*":
    print(a * b)
elif znamenko == "/":
    if b == 0:
        print("Nulou dělit nelze.")
    else:
        print(a / b)
else:
    print("Neznámé znaménko.")
