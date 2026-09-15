# ---------------------------------------------
#  Funkce bez parametru
# ---------------------------------------------
# Spusť soubor a odpověz na otázku.
#
# Někdy funkce nic zvenku nepotřebuje a pokaždé udělá to samé.
# Závorky pak zůstanou prázdné – v definici i při volání.

def pravidla():
    print("Hádej číslo od 1 do 20.")
    print("Po každém tipu ti řeknu, jestli je moc velké, nebo malé.")
    print("Máš pět pokusů.")


pravidla()

odpoved = input("Chceš pravidla zopakovat? (ano/ne) ")
if odpoved == "ano":
    pravidla()

print("Tak jdeme hrát.")
