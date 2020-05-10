import numpy as np

aantal_rijen = 6
aantal_kolommen = 7


def maak_bord():
    bord = np.zeros((6, 7))  # np.zeros maakt een matrix aan gevuld met nullen
    return bord


def leg_steen(bord, rij, kolom, steen):
    bord[rij][kolom] = steen


def geldige_locatie(bord, kolom):
    return bord[5][kolom] == 0


def volgende_open_rij(bord, kolom):
    for r in range(aantal_rijen):
        if bord[r][kolom] == 0:
            return r


def print_bord(bord):
    print(np.flip(bord, 0))


bord = maak_bord()
print_bord(bord)
game_over = False
beurd = 0

while not game_over:
    # Vraag speler 1 input
    if beurd == 0:
        kolom = int(input("Speler 1 maak jouw selectie (0-6): "))

        if geldige_locatie(bord,kolom):
            rij = volgende_open_rij(bord, kolom)
            leg_steen(bord, rij, kolom, 1)

    # Vraag speler 2 input
    else:
        kolom = int(input("Speler 2 maak jouw selectie (0-6): "))

        if geldige_locatie(bord,kolom):
            rij = volgende_open_rij(bord, kolom)
            leg_steen(bord, rij, kolom, 2)

    print_bord(bord)

    beurd += 1
    beurd = beurd % 2

