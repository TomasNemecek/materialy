# ---------------------------------------------
#  Vzorové řešení: input
# ---------------------------------------------
# Tvoje řešení může vypadat trochu jinak, a to je v pořádku.


# 1) Zeptej se uživatele na jméno a ulož ho do proměnné.
jmeno = input("Jak se jmenuješ? ")


# 2) Pozdrav uživatele jeho jménem (např. Ahoj, Anna).
print("Ahoj,", jmeno)


# 3) Zeptej se ještě na jednu věc (třeba oblíbenou barvu)
#    a vypiš ji ve větě.
barva = input("Jaká je tvoje oblíbená barva? ")
print("Tvoje oblíbená barva je", barva)


# 4) Zeptej se uživatele na jeho věk, převeď ho na číslo
#    a vypiš, kolik mu bude za 10 let.
vek = int(input("Kolik ti je let? "))
print("Za 10 let ti bude", vek + 10)


# 5) Napiš program, který se zeptá na jméno a na věk (převeď na číslo)
#    a vypíše větu: Ahoj <jmeno>, za rok ti bude <věk + 1> let.
jmeno = input("Jak se jmenuješ? ")
vek = int(input("Kolik ti je let? "))
print("Ahoj,", jmeno, "- za rok ti bude", vek + 1, "let")
