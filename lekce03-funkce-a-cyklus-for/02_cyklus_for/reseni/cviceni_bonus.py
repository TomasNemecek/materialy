# ---------------------------------------------
#  Řešení – bonusová cvičení: cyklus for
# ---------------------------------------------


# B1) Uživatel zadá číslo N. Spočítej cyklem jeho faktoriál –
#     tedy 1 * 2 * 3 * ... * N – a výsledek vypiš.
#     (Faktoriál z 5 je 120.)
n = int(input("Zadej číslo: "))
faktorial = 1
for cislo in range(1, n + 1):     # +1, aby se počítalo i samotné N
    faktorial = faktorial * cislo
print(faktorial)                  # pro 5 vypíše 120


# B2) Spočítej cyklem součet všech sudých čísel od 1 do 100 a vypiš ho.
soucet = 0
for cislo in range(2, 101, 2):    # krok 2 = jen sudá čísla
    soucet = soucet + cislo
print(soucet)                     # 2550


# B3) Uživatel zadá počáteční částku na spořicím účtu. Úrok je 5 % ročně.
#     Spočítej cyklem, kolik na účtu bude po deseti letech
#     (každý rok se částka vynásobí 1.05), a výsledek vypiš.
castka = int(input("Kolik si ukládáš? "))
for rok in range(10):
    castka = castka * 1.05
print(round(castka, 2))           # pro 1000 vypíše 1628.89
