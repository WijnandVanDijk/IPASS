import numpy as np

aantal_rijen = 6
aantal_kolommen = 7


def maak_bord():
    bord = np.zeros((aantal_rijen, aantal_kolommen))  # np.zeros maakt een matrix aan gevuld met nullen
    return bord


def leg_steen(bord, rij, kolom, steen):
    bord[rij][kolom] = steen


def geldige_locatie(bord, kolom):
    return bord[aantal_rijen - 1][kolom] == 0


def volgende_open_rij(bord, kolom):
    for r in range(aantal_rijen):
        if bord[r][kolom] == 0:
            return r


def print_bord(bord):
    print(np.flip(bord, 0))


def winnende_zet(bord, steen):
    for c in range(aantal_kolommen - 3):
        for r in range(aantal_rijen):
            if bord[r][c] == steen and bord[r][c + 1] == steen and bord[r][c + 2] == steen and bord[r][c + 3] == steen:
                return True

    for c in range(aantal_kolommen):
        for r in range(aantal_rijen - 3):
            if bord[r][c] == steen and bord[r + 1][c] == steen and bord[r + 2][c] == steen and bord[r + 3][c] == steen:
                return True

    for c in range(aantal_kolommen - 3):
        for r in range(aantal_rijen - 3):
            if bord[r][c] == steen and bord[r + 1][c + 1] == steen and bord[r + 2][c + 2] == steen and bord[r + 3][c + 3] == steen:
                return True

    for c in range(aantal_kolommen - 3):
        for r in range(3, aantal_rijen):
            if bord[r][c] == steen and bord[r - 1][c + 1] == steen and bord[r - 2][c + 2] == steen and bord[r - 3][c + 3] == steen:
                return True


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

            if winnende_zet(bord, 1):
                print("Speler 1 wint!")
                game_over = True

    # Vraag speler 2 input
    else:
        kolom = int(input("Speler 2 maak jouw selectie (0-6): "))

        if geldige_locatie(bord,kolom):
            rij = volgende_open_rij(bord, kolom)
            leg_steen(bord, rij, kolom, 2)

            if winnende_zet(bord, 2):
                print("Speler 2 wint!")
                game_over = True

    print_bord(bord)

    beurd += 1
    beurd = beurd % 2

