# ---------------------------------------------
#  Řešení – cyklus for
# ---------------------------------------------


# 1) Cyklem vypiš čísla od 1 do 10, každé na svůj řádek.
for cislo in range(1, 11):
    print(cislo)


# 2) Cyklem vypiš pětkrát text "PyLadies".
for cislo in range(5):
    print("PyLadies")


# 3) Cyklem vypiš násobky tří od 3 do 30 (tedy 3, 6, 9, ... až 30).
for cislo in range(3, 31, 3):
    print(cislo)


# 4) Spočítej součet všech čísel od 1 do 100 pomocí cyklu for
#    (ne funkcí sum) a výsledek vypiš.
soucet = 0
for cislo in range(1, 101):
    soucet = soucet + cislo
print(soucet)                 # 5050


# 5) Uživatel zadá číslo. Cyklem vypiš jeho malou násobilku –
#    tedy cislo * 1 až cislo * 10, každý řádek třeba "7 * 3 = 21".
cislo = int(input("Zadej číslo: "))
for nasobek in range(1, 11):
    print(cislo, "*", nasobek, "=", cislo * nasobek)


# 6) Vypočítej 2 na desátou tak, že v cyklu desetkrát vynásobíš dvěma.
#    Výsledek vypiš (má vyjít 1024).
vysledek = 1
for cislo in range(10):
    vysledek = vysledek * 2
print(vysledek)               # 1024
