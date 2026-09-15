# ---------------------------------------------
#  Bonusová cvičení: opakování
# ---------------------------------------------
# Pro rychlíky – když máš hotové cviceni.py a zbývá čas.


# B1) Kámen, nůžky, papír – znáš z bonusu v lekci 2, kde hráli
#     dva lidé. Teď to rozšíříme: hraješ proti počítači a na víc kol.
#     - Zeptej se na svůj tah: "kamen", "nuzky" nebo "papir".
#     - Počítač si tah vylosuje: randrange(1, 4) vrátí 1, 2 nebo 3,
#       tak si to číslo přelož na tah (1 = kamen, 2 = nuzky, 3 = papir).
#     - Vypiš, co hrál počítač, a kdo kolo vyhrál.
#     - Pak se zeptej "Hrát znovu? (ano/ne) " a podle odpovědi
#       buď pokračuj, nebo skonči.
#     Kdo koho poráží: kámen tupí nůžky, nůžky stříhají papír,
#     papír balí kámen.
#     Nahoru na první řádek nezapomeň:  from random import randrange



# B2) Uživatel zadá číslo N. Vypiš z hvězdiček trojúhelník vysoký N –
#     první řádek "*", druhý "**", ... N-tý má N hvězdiček.
#     (Nápověda: text se dá opakovat: "*" * 3 je "***")



# B3) Uživatel zadá celé číslo. Sečti jeho číslice a součet vypiš.
#     Například z 253 vyjde 10, protože 2 + 5 + 3 = 10.
#     (Nápověda: cislo % 10 dá poslední číslici, cislo // 10 ji utrhne.)
#     Zkus i záporné číslo. Aby to fungovalo, hodí se abs(cislo) –
#     ta funkce zahodí minus.
