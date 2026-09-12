# ---------------------------------------------
#  Vzorové řešení: bonusová cvičení proměnné
# ---------------------------------------------
# Tvoje řešení může vypadat trochu jinak, a to je v pořádku.


# B1) Máš dvě proměnné: a = 5 a b = 3.
#     Prohoď jejich hodnoty tak, aby v a bylo 3 a v b bylo 5.
#     Nakonec obě vypiš.
a = 5
b = 3
pomocna = a   # dočasně si schováme hodnotu a
a = b
b = pomocna
print(a, b)


# B2) Vytvoř proměnnou skore a nastav ji na 0.
#     Postupně k ní přičti 10, potom 25 a potom 5 –
#     pokaždé novou hodnotu ulož zpět do skore.
#     Nakonec skore vypiš.
skore = 0
skore = skore + 10
skore = skore + 25
skore = skore + 5
print(skore)


# B3) Vytvoř proměnné jmeno a prijmeni.
#     Vypiš na jeden řádek celé jméno.
jmeno = "Anna"
prijmeni = "Nováková"
print(jmeno, prijmeni)
