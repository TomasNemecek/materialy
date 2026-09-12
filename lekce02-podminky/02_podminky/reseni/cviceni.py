# ---------------------------------------------
#  Řešení – podmínky (if / elif / else)
# ---------------------------------------------


# 1) Máš proměnnou vek. Vypiš "Jsi plnoletá.", když je vek 18 a víc,
#    jinak vypiš "Ještě ne.".
vek = 16
if vek >= 18:
    print("Jsi plnoletá.")
else:
    print("Ještě ne.")


# 2) Vrať se ke studentce se třemi známkami. Spočítej průměr a vypiš
#    "Máš vyznamenání!", když je průměr menší nebo rovný 2,
#    jinak vypiš "Bez vyznamenání.".
znamka1 = 1
znamka2 = 3
znamka3 = 2
prumer = (znamka1 + znamka2 + znamka3) / 3
if prumer <= 2:
    print("Máš vyznamenání!")
else:
    print("Bez vyznamenání.")


# 3) Zeptej se uživatele na číslo. Vypiš "Velké číslo!", když je větší
#    než 100, jinak "Malé číslo.".
cislo = int(input("Zadej číslo: "))
if cislo > 100:
    print("Velké číslo!")
else:
    print("Malé číslo.")


# 4) Máš proměnnou barva se stavem semaforu ("červená", "oranžová"
#    nebo "zelená"). Vypiš, co má řidič udělat:
#    "červená" → "Stůj", "oranžová" → "Připrav se", "zelená" → "Jeď",
#    cokoli jiného → "Neznámý signál".
barva = "zelená"
if barva == "červená":
    print("Stůj")
elif barva == "oranžová":
    print("Připrav se")
elif barva == "zelená":
    print("Jeď")
else:
    print("Neznámý signál")


# 5) Zeptej se na počet bodů z testu (0 až 100) a vypiš známku:
#    90 a víc → 1, 75 a víc → 2, 60 a víc → 3, 40 a víc → 4,
#    jinak → 5.
body = int(input("Kolik bodů? "))
if body >= 90:
    print(1)
elif body >= 75:
    print(2)
elif body >= 60:
    print(3)
elif body >= 40:
    print(4)
else:
    print(5)


# 6) Vnořená podmínka s otázkami na uživatele.
#    Zeptej se: "Máš hlad? (ano/ne)" a ulož odpověď do proměnné hlad.
#    Když má hlad, zeptej se ještě "Máš doma jídlo? (ano/ne)":
#      - když má jídlo, vypiš "Uvař si."
#      - když nemá, vypiš "Objednej si."
#    Když nemá hlad, vypiš "Tak nic, uvidíme později.".
hlad = input("Máš hlad? (ano/ne) ")
if hlad == "ano":
    jidlo = input("Máš doma jídlo? (ano/ne) ")
    if jidlo == "ano":
        print("Uvař si.")
    else:
        print("Objednej si.")
else:
    print("Tak nic, uvidíme později.")
