import numpy as np
import pygame
import sys
import math
import random
import unittest


# kopie van connectfour_with_ai_hard() voor tests.


PURPLE = (75, 0, 130) #
LIGHT_BLUE = (29, 172, 231) #
BLUE = (0, 0, 255) #
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255) #
PINK = (255,20,147) #
GREEN = (0,128,0) #
ORANGE = (255,165,0) #
COLOR = LIGHT_BLUE

aantal_kolommen = 7
aantal_rijen = 6


MENS = 0
AI = 1

LEEG = 0
MENS_STEEN = 1
AI_STEEN = 2

def maak_bord(): # bord wordt aangemaakt
    bord = np.zeros((aantal_rijen, aantal_kolommen))  # np.zeros maakt een matrix aan gevuld met nullen
    return bord

def leg_steen(bord, rij, kolom, steen): # legt de steen.
    bord[rij][kolom] = steen

def geldige_locatie_func(bord, kolom): # kijkt of de locatie geldig is voor de zet.
    return bord[aantal_rijen - 1][kolom] == 0 # kijkt of er nog minimaal 1 plek over is in de kolom.

def volgende_open_rij(bord, kolom): # kijkt op welke rij de steen gelegd wordt.
    for r in range(aantal_rijen):
        if bord[r][kolom] == 0: # als de plek nog een 0 is (0=leeg) de eerste 0 wordt gereturnd.
            return r

def print_bord(bord): # flipt het bord zodat de stenen naar beneden 'vallen'.
    print(np.flip(bord, 0))

def winnende_zet(bord, steen):  # kijkt of er een 4 op een rij is. kijkt naar alle mogelijkheden plekken waar een vier op een rij kan zijn.
    # kijkt naar alle HORIZONTALEN locaties voor een 4 op een rij.
    for k in range(
            aantal_kolommen - 3):  # -3 omdat je bij de laatste 3 geen vier op een rij meer kan krijgen(links naar rechts).
        for r in range(aantal_rijen):
            if bord[r][k] == steen and bord[r][k + 1] == steen and bord[r][k + 2] == steen and bord[r][
                k + 3] == steen:
                return True
    # kijkt naar alle VERTICALEN locaties voor een 4 op een rij.
    for k in range(aantal_kolommen):
        for r in range(
                aantal_rijen - 3):  # -3 omdat je bij de laatste 3 geen vier op een rij meer kan krijgen(beneden naar boven).
            if bord[r][k] == steen and bord[r + 1][k] == steen and bord[r + 2][k] == steen and bord[r + 3][
                k] == steen:
                return True

    # kijkt naar alle links-rechts boven locaties voor een 4 op een rij.
    for k in range(aantal_kolommen - 3):
        for r in range(aantal_rijen - 3):
            if bord[r][k] == steen and bord[r + 1][k + 1] == steen and bord[r + 2][k + 2] == steen and bord[r + 3][
                k + 3] == steen:
                return True

    # kijkt naar alle rechts-links boven locaties voor een 4 op een rij.
    for k in range(aantal_kolommen - 3):
        for r in range(3, aantal_rijen):
            if bord[r][k] == steen and bord[r - 1][k + 1] == steen and bord[r - 2][k + 2] == steen and bord[r - 3][
                k + 3] == steen:
                return True

def window_score(window, steen):
    score = 0
    tegenstander_steen = MENS_STEEN
    if steen == MENS_STEEN:
        tegenstander_steen = AI_STEEN


    if window.count(steen) == 4:
        score += 100  # vier op een rij is dus 100 punten
    elif window.count(steen) == 3 and window.count(LEEG) == 1:
        score += 5  # drie op rij is 10 punten
    elif window.count(steen) == 2 and window.count(LEEG) == 2:
        score += 2 # twee op rij is 2 punten

    if window.count(tegenstander_steen) == 3 and window.count(LEEG) == 1:
        score -= 4 # als de tegenstander 3 op een rij heeft -4 punten

    return score


def punten_positie(bord, steen):
    score = 0

    # Score voor middelste kolom (omdat die het meest mogelijkheden maakt en dus het beste is)
    middelste_kolom_array = [int(i) for i in list(bord[:, aantal_kolommen // 2])]
    middelste_kolom_count = middelste_kolom_array.count(steen)
    score += middelste_kolom_count * 3

    # Score Horizontaal
    for r in range(aantal_rijen):
        rij_array = [int(i) for i in list(bord[r,:])]
        for c in range(aantal_kolommen - 3):
            window = rij_array[c : c + 4]
            score += window_score(window, score)


    # Score Verticaal
    for k in range(aantal_kolommen):
        kolom_array = [int(i) for i in list(bord[:, k])]
        for r in range(aantal_kolommen - 3):
            window = kolom_array[r : r + 4]
            score += window_score(window, score)

    # Score diagonaal van links onder naar rechts boven
    for r in range(aantal_rijen - 3):
        for k in range(aantal_kolommen - 3):
            window = [bord[r+i][k+i] for i in range(4)]
            score += window_score(window, score)

    for r in range(aantal_rijen - 3):
        for k in range(aantal_kolommen - 3):
            window = [bord[r + 3 - i][k + i] for i in range(4)]
            score += window_score(window, score)


    return score

def is_terminal_node(bord):
    return winnende_zet(bord, MENS_STEEN) or winnende_zet(bord, AI_STEEN) or len(get_geldige_zet(bord)) == 0
    # terminal node is: iemand wint of als er geen plekken meer over zijn om stenen te plaatsen

def minimax_algoritme(bord, depth, alpha, beta, maximizingplayer):  # pseudocode van: https://en.wikipedia.org/wiki/Minimax
    geldige_locatie_func = get_geldige_zet(bord)
    is_terminal = is_terminal_node(bord)
    if depth == 0 or is_terminal:
        if is_terminal:
            if winnende_zet(bord, AI_STEEN):
                return None, 1000000 # none omdat we dezelfde format nodig hebben
            elif winnende_zet(bord, MENS_STEEN):
                return None, -1000000
            else: # als er geen zetten meer mogelijk zijn
                return None, 0
        else:
            return None, punten_positie(bord, AI_STEEN)

    if maximizingplayer:
        value = -math.inf
        kol =  random.choice(geldige_locatie_func)
        for kolom in geldige_locatie_func:
            rij = volgende_open_rij(bord, kolom)
            bord_copy = bord.copy()
            leg_steen(bord_copy, rij, kolom, AI_STEEN)
            nieuwe_value = minimax_algoritme(bord_copy, depth - 1, alpha, beta,  False)[1]
            if nieuwe_value > value:
                value = nieuwe_value
                kol = kolom
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return kol, value

    else:
        value = math.inf
        kol = random.choice(geldige_locatie_func)
        for kolom in geldige_locatie_func:
            rij = volgende_open_rij(bord, kolom)
            bord_copy = bord.copy()
            leg_steen(bord_copy, rij, kolom, MENS_STEEN)
            nieuwe_value = minimax_algoritme(bord_copy, depth - 1, alpha, beta, True)[1]
            if nieuwe_value < value:
                value = nieuwe_value
                kol = kolom
            beta = min(beta, value)
            if alpha >= beta:
                break
        return kol, value




def get_geldige_zet(bord):
    geldige_locatie = []
    for kolom in range(aantal_kolommen):
        if geldige_locatie_func(bord, kolom):
            geldige_locatie.append(kolom)

    return geldige_locatie

def kies_beste_zet(bord, steen): # geeft voorkeur aan horizontaal 3 op een rij's
    geldige_locatie = get_geldige_zet(bord)
    beste_score = -10000
    beste_kolom = random.choice(geldige_locatie)
    for kolom in geldige_locatie:
        rij = volgende_open_rij(bord,kolom)
        tijdelijk_bord = bord.copy() # als je niet een copy maakt gebruikt hij dezelfde geheugen locatie als het 'echte' bord
        leg_steen(tijdelijk_bord, rij, kolom, steen)
        score = punten_positie(tijdelijk_bord, steen)
        if score > beste_score:
            beste_score = score
            beste_kolom = kolom

    return beste_kolom

def teken_bord(bord): # maakt het bord in PyGame.
    for k in range(aantal_kolommen):
        for r in range(aantal_rijen):
            pygame.draw.rect(Gamescherm, COLOR,
                             (k * squaresize, r * squaresize + squaresize, squaresize, squaresize))
            pygame.draw.circle(Gamescherm, BLACK, (
                int(k * squaresize + squaresize / 2), int(r * squaresize + squaresize + squaresize / 2)), radius)

    for k in range(aantal_kolommen):
        for r in range(aantal_rijen):
            if bord[r][k] == 1: # wie aan de beurd is, in dit geval speler 1.
                pygame.draw.circle(Gamescherm, RED, (
                    int(k * squaresize + squaresize / 2), hoogte - int(r * squaresize + squaresize / 2)), radius)
            elif bord[r][k] == 2: # wie aan de beurd is, in dit geval speler 2.
                pygame.draw.circle(Gamescherm, YELLOW, (
                    int(k * squaresize + squaresize / 2), hoogte - int(r * squaresize + squaresize / 2)), radius)
    pygame.display.update()

bord = maak_bord()
print_bord(bord)
game_over = False
beurd = 0

pygame.init()  # bron voor pygame: https://www.pygame.org/docs/ref/draw.html

squaresize = 100  # in pixels

breedte = aantal_kolommen * squaresize
hoogte = (aantal_rijen + 1) * squaresize  # +1 zodat je ziet waar je de zet doet

size = (breedte, hoogte)

radius = int(squaresize / 2 - 5)

Gamescherm = pygame.display.set_mode(size)
teken_bord(bord)
pygame.display.update()

myfont = pygame.font.SysFont('monospace', 75)

beurd = random.randint(MENS, AI)

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(Gamescherm, BLACK, (0, 0, breedte, squaresize))
            posx = event.pos[0]
            if beurd == MENS:
                pygame.draw.circle(Gamescherm, RED, (posx, int(squaresize / 2)), radius)

        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(Gamescherm, BLACK, (0, 0, breedte, squaresize))
            if beurd == MENS:
                posx = event.pos[0]
                kolom = int(math.floor(posx / squaresize))

                if geldige_locatie_func(bord, kolom):
                    rij = volgende_open_rij(bord, kolom)
                    leg_steen(bord, rij, kolom, 1)

                    if winnende_zet(bord, 1):
                        label = myfont.render("Speler 1 wint!", 1, RED)
                        Gamescherm.blit(label, (40, 10))
                        game_over = True

                    beurd += 1
                    beurd = beurd % 2

                    print_bord(bord)
                    teken_bord(bord)

    if beurd == AI and not game_over:

        #kolom = random.randint(0, aantal_kolommen-1)
        #kolom = kies_beste_zet(bord, AI_STEEN)
        kolom, minimax_score = minimax_algoritme(bord, 4, -math.inf, math.inf, True)

        if geldige_locatie_func(bord, kolom):
            pygame.time.wait(500)
            rij = volgende_open_rij(bord, kolom)
            leg_steen(bord, rij, kolom, 2)

            if winnende_zet(bord, 2):
                label = myfont.render("Speler 2 wint!", 1, YELLOW)
                Gamescherm.blit(label, (40, 10))
                game_over = True

            print_bord(bord)
            teken_bord(bord)

            beurd += 1
            beurd = beurd % 2

    if game_over:
        pygame.time.wait(3000)  # in miliseconds, dus 3 seconden
        pygame.display.quit()
        pygame.quit()
        pygame.quit()

# speel eerst een potje zodat de tests gaan werken

class UNITtests(unittest.TestCase):


    def test_breedte(self):
        self.assertEqual(breedte, aantal_kolommen * squaresize)

    def test_hoogte(self):
        self.assertEqual(hoogte, (aantal_rijen + 1) * squaresize)

    def test_game_over(self):
        self.assertEqual(game_over, True) # True omdat de tests na de game pas gaan lopen, na het spel is game_over True daarvoor False

    def test_size(self):
        self.assertEqual(size, (breedte, hoogte))

    def test_squaresize(self):
        self.assertEqual(squaresize, 100)

if __name__ == "__main__":
    unittest.main()



