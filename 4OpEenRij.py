import numpy as np
import pygame
import sys
import math
import random

from pygame import mixer
from pygame.locals import *


COLOR = ()
PURPLE = (75, 0, 130)
BLUE = (29, 172, 231)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

aantal_rijen = 6
aantal_kolommen = 7

def connectfour_with_ai():

    MENS = 0
    AI = 1

    LEEG = 0
    MENS_STEEN = 1
    AI_STEEN = 2

    def maak_bord():
        bord = np.zeros((aantal_rijen, aantal_kolommen))  # np.zeros maakt een matrix aan gevuld met nullen
        return bord

    def leg_steen(bord, rij, kolom, steen):
        bord[rij][kolom] = steen

    def geldige_locatie_func(bord, kolom):
        return bord[aantal_rijen - 1][kolom] == 0

    def volgende_open_rij(bord, kolom):
        for r in range(aantal_rijen):
            if bord[r][kolom] == 0:
                return r

    def print_bord(bord):
        print(np.flip(bord, 0))

    def winnende_zet(bord, steen):
        for k in range(aantal_kolommen - 3):
            for r in range(aantal_rijen):
                if bord[r][k] == steen and bord[r][k + 1] == steen and bord[r][k + 2] == steen and bord[r][
                    k + 3] == steen:
                    return True

        for k in range(aantal_kolommen):
            for r in range(aantal_rijen - 3):
                if bord[r][k] == steen and bord[r + 1][k] == steen and bord[r + 2][k] == steen and bord[r + 3][
                    k] == steen:
                    return True

        for k in range(aantal_kolommen - 3):
            for r in range(aantal_rijen - 3):
                if bord[r][k] == steen and bord[r + 1][k + 1] == steen and bord[r + 2][k + 2] == steen and bord[r + 3][
                    k + 3] == steen:
                    return True

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
            score -= 4

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

    def minimax_algoritme(node, depth, maximizingplayer):  # pseudocode van: https://en.wikipedia.org/wiki/Minimax
        geldige_locatie_func = get_geldige_zet(bord)
        is_terminal = is_terminal_node(bord)
        if depth == 0 or is_terminal:
            if is_terminal:
                if winnende_zet(bord, AI_STEEN):
                    return 1000000
                elif winnende_zet(bord, MENS_STEEN):
                    return -1000000
                else: # als er geen zetten meer mogelijk zijn
                    return 0
            else:
                return punten_positie(bord, AI_STEEN)
        if maximizingplayer:
            value = -math.inf
            for kolom in geldige_locatie_func:
                rij = volgende_open_rij(bord, kolom)
                bord_copy = bord.copy()
                leg_steen(bord_copy, rij, kolom, AI_STEEN)
                nieuwe_value = max(value, minimax_algoritme(bord_copy, depth - 1, False))
                return nieuwe_value
        else:
            value = math.inf
            for kolom in geldige_locatie_func:
                rij = volgende_open_rij(bord, kolom)
                bord_copy = bord.copy()
                leg_steen(bord_copy, rij, kolom, MENS_STEEN)
                nieuwe_value = min(value, minimax_algoritme(bord_copy, depth - 1, True))
                return nieuwe_value



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

    def teken_bord(bord):
        for k in range(aantal_kolommen):
            for r in range(aantal_rijen):
                pygame.draw.rect(Gamescherm, BLUE,
                                 (k * squaresize, r * squaresize + squaresize, squaresize, squaresize))
                pygame.draw.circle(Gamescherm, BLACK, (
                    int(k * squaresize + squaresize / 2), int(r * squaresize + squaresize + squaresize / 2)), radius)

        for k in range(aantal_kolommen):
            for r in range(aantal_rijen):
                if bord[r][k] == 1:
                    pygame.draw.circle(Gamescherm, RED, (
                        int(k * squaresize + squaresize / 2), hoogte - int(r * squaresize + squaresize / 2)), radius)
                elif bord[r][k] == 2:
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
                    kolom = kies_beste_zet(bord, AI_STEEN)

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
                    pygame.time.wait(5000)  # in miliseconds, dus 5 seconden
                    pygame.display.quit()
                    pygame.quit()



def connectfour_no_ai():

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
        for k in range(aantal_kolommen - 3):
            for r in range(aantal_rijen):
                if bord[r][k] == steen and bord[r][k + 1] == steen and bord[r][k + 2] == steen and bord[r][
                    k + 3] == steen:
                    return True

        for k in range(aantal_kolommen):
            for r in range(aantal_rijen - 3):
                if bord[r][k] == steen and bord[r + 1][k] == steen and bord[r + 2][k] == steen and bord[r + 3][
                    k] == steen:
                    return True

        for k in range(aantal_kolommen - 3):
            for r in range(aantal_rijen - 3):
                if bord[r][k] == steen and bord[r + 1][k + 1] == steen and bord[r + 2][k + 2] == steen and bord[r + 3][
                    k + 3] == steen:
                    return True

        for k in range(aantal_kolommen - 3):
            for r in range(3, aantal_rijen):
                if bord[r][k] == steen and bord[r - 1][k + 1] == steen and bord[r - 2][k + 2] == steen and bord[r - 3][
                    k + 3] == steen:
                    return True

    def teken_bord(bord):
        for k in range(aantal_kolommen):
            for r in range(aantal_rijen):
                pygame.draw.rect(Gamescherm, BLUE,
                                 (k * squaresize, r * squaresize + squaresize, squaresize, squaresize))
                pygame.draw.circle(Gamescherm, BLACK, (
                    int(k * squaresize + squaresize / 2), int(r * squaresize + squaresize + squaresize / 2)), radius)

        for k in range(aantal_kolommen):
            for r in range(aantal_rijen):
                if bord[r][k] == 1:
                    pygame.draw.circle(Gamescherm, RED, (
                        int(k * squaresize + squaresize / 2), hoogte - int(r * squaresize + squaresize / 2)), radius)
                elif bord[r][k] == 2:
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

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(Gamescherm, BLACK, (0, 0, breedte, squaresize))
                posx = event.pos[0]
                if beurd == 0:
                    pygame.draw.circle(Gamescherm, RED, (posx, int(squaresize / 2)), radius)
                else:
                    pygame.draw.circle(Gamescherm, YELLOW, (posx, int(squaresize / 2)), radius)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(Gamescherm, BLACK, (0, 0, breedte, squaresize))
                if beurd == 0:
                    posx = event.pos[0]
                    kolom = int(math.floor(posx / squaresize))

                    if geldige_locatie(bord, kolom):
                        rij = volgende_open_rij(bord, kolom)
                        leg_steen(bord, rij, kolom, 1)

                        if winnende_zet(bord, 1):
                            label = myfont.render("Speler 1 wint!", 1, RED)
                            Gamescherm.blit(label, (40, 10))
                            game_over = True

                else:
                    posx = event.pos[0]
                    kolom = int(math.floor(posx / squaresize))

                    if geldige_locatie(bord, kolom):
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
                    pygame.time.wait(5000)  # in miliseconds, dus 5 seconden
                    pygame.display.quit()
                    pygame.quit()



def gui():
    mainClock = pygame.time.Clock()

    pygame.init()
    pygame.display.set_caption('Hogeschool Utrecht IPASS Connect Four project, Wijnand van Dijk')
    screen = pygame.display.set_mode((960, 494), 0, 32)
    font = pygame.font.SysFont(None, 20)

    # Achtergrond muziek wordt aangezet
    mixer.music.load("BackgroundMusic.wav")
    mixer.music.play(-1) # de '-1' laat de music loopen
    pygame.mixer.music.set_volume(0.666)

    mx, my = pygame.mouse.get_pos()

    def draw_text(text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    klik = False

    def main_menu():
        global klik
        while True:


            LOGO = pygame.image.load('background.png')

            screen.fill((0, 0, 0))
            screen.blit(LOGO, (338, 10))
            draw_text('', font, WHITE, screen, 430, 20)
            draw_text('Play', font, WHITE, screen, 90, 385)
            draw_text('Over mij', font, WHITE, screen, 263, 385)
            draw_text('Weetjes', font, WHITE, screen, 455, 385)
            draw_text('Options', font, WHITE, screen, 645, 385)
            draw_text('Quit', font, WHITE, screen, 845, 385)

            mx, my = pygame.mouse.get_pos()

            button_play = pygame.Rect(50, 400, 100, 50)
            button_overons = pygame.Rect(240, 400, 100, 50)
            button_weetjes = pygame.Rect(430, 400, 100, 50)
            button_options = pygame.Rect(620, 400, 100, 50)
            button_quit = pygame.Rect(810, 400, 100, 50)
            if button_play.collidepoint(mx, my):
                if klik:
                    connectfour_no_ai()
            if button_overons.collidepoint(mx, my):
                if klik:
                    overons()
            if button_weetjes.collidepoint(mx, my):
                if klik:
                    weetjes()
            if button_options.collidepoint(mx, my):
                if klik:
                    options()
            if button_quit.collidepoint(mx, my):
                if klik:
                    sluiten()
            pygame.draw.rect(screen, BLUE, button_play)
            pygame.draw.rect(screen, BLUE, button_overons)
            pygame.draw.rect(screen, BLUE, button_options)
            pygame.draw.rect(screen, BLUE, button_weetjes)
            pygame.draw.rect(screen, BLUE, button_quit)

            klik = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        klik = True

            pygame.display.update()
            mainClock.tick(60)

    def overons():
        running = True
        while running:
            screen.fill((0, 0, 0))

            draw_text('Over mij', font, WHITE, screen, 430, 20)
            draw_text("Hallo, ik ben Wijnand van Dijk maker en bedenker van dit project en eerste jaars artificial intelligence"
                      " student aan de Hogeschool Utrecht.",
                      font, WHITE, screen, 50, 70)
            draw_text("Voor mijn studie moest is ik een eindproject maken als laatste test om over te mogen naar het "
                      "volgende jaar.",
                      font, WHITE, screen, 50, 90)
            draw_text("Ik heb voor deze studie gekozen omdat ik altijd al een jongen ben geweest van de technologie en de toekomst.",
                      font, WHITE, screen, 50, 110)
            draw_text("door die redenen ben ik opzoek gegaan naar een studie waar die twee aspecten in voor komen, en wat is beter dan",
                      font, WHITE, screen, 50, 130)
            draw_text("de ICT en vooral de AI richting? Ik ben deze opleiding begonnen met minimale voorkennis over programmeren en ICT in het algemeen",
                      font, WHITE, screen, 50, 150)
            draw_text("Toen ik op dit onderwerp was gekomen wist ik meteen dat dit het zou worden omdat er een mooie AI"
                      "tegestander gemaakt kan worden",
                      font, WHITE, screen, 50, 190)
            draw_text("voor Connect Four ook wel bekend als vier op een rij. Nadat ik zeker wist dat dit mijn onderwerp ging worden ben ik gelijk op onderzoek",
                      font, WHITE, screen, 50, 210)
            draw_text("uit gegaan met het doel om de geschiedenis van Connect Four te weten (zie 'Weetjes') en een algoritme te vinden voor de AI-opponent.",
                      font, WHITE, screen, 50, 230)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            mainClock.tick(60)

    def weetjes():

        running = True
        while running:

            fact = pygame.image.load('fact.png')
            win_lose = pygame.image.load('ScreenHunter 38.jpg')
            screen.fill((0, 0, 0))
            screen.blit(fact, (367.5, 10))
            screen.blit(win_lose, (710, 250))



            draw_text('', font, WHITE, screen, 430, 20)
            draw_text("De geschiedenis:",
                      font, WHITE, screen, 50, 130)
            draw_text("Het spel werd voor het eerst officiiel uitgegeven als Connect Four in 1974 door spelfabrikant Milton Bradley,",
                      font, WHITE, screen, 50, 150)
            draw_text("tegenwoordig een onderdeel van spelfabrikant Hasbro. Voor die tijd was het spel al bekend als The Captain's Mistress.",
                      font, WHITE, screen, 50, 170)
            draw_text("In 1988, 14 jaar na de release, is het spel 'opgelost'. Een opgelost spel is een spel waarvan de uitkomst vanuit elke positie correct",
                      font, WHITE, screen, 50, 190)
            draw_text("kan worden voorspeld, ervan uitgaande dat beide spelers perfect spelen.",
                      font, WHITE, screen, 50, 210)
            draw_text("Als we ervan uitgaan dat beide spelen perfect spelen wint de middelste (vierde) rij, worden de derde en vijfde rij een gelijk spel en",
                      font, WHITE, screen, 50, 230)
            draw_text("verliezen de eerste, tweede, zesde en zevende rij.",
                      font, WHITE, screen, 50, 250)
            draw_text("Weetjes:",
                      font, WHITE, screen, 50, 290)
            draw_text("Er zijn 4.531.985.219.092 mogelijk spel situaties, waarvan 1.905.333.170.621 een vier op een rij bevattten.",
                      font, WHITE, screen, 50, 310)
            draw_text("Er zijn 713.298.878 manieren om een vier op een rij bord weer te geven (qua steen posities)",
                      font, WHITE, screen, 50, 330)
            draw_text("Voor de bronnen raadpleeg de README.",
                      font, WHITE, screen, 50, 400)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            mainClock.tick(60)

    def options():
        global klik
        running = True
        while running:

            screen.fill((0, 0, 0))
            draw_text('Options', font, WHITE, screen, 430, 20)
            draw_text('Muziek volume:', font, WHITE, screen, 50, 100)
            draw_text('Uit', font, WHITE, screen, 85, 125)
            draw_text('1', font, WHITE, screen, 90, 175)
            draw_text('2', font, WHITE, screen, 90, 225)
            draw_text('3', font, WHITE, screen, 90, 275)

            mx, my = pygame.mouse.get_pos()

            button_VOLuit = pygame.Rect(68, 140, 50, 25)
            button_VOL1 = pygame.Rect(68, 195, 50, 25)
            button_VOL2= pygame.Rect(68, 245, 50, 25)
            button_VOL3 = pygame.Rect(68, 295, 50, 25)
            if button_VOLuit.collidepoint(mx, my):
                if klik:
                    pygame.mixer.music.set_volume(0)
            if button_VOL1.collidepoint(mx, my):
                if klik:
                    pygame.mixer.music.set_volume(0.333)
            if button_VOL2.collidepoint(mx, my):
                if klik:
                    pygame.mixer.music.set_volume(0.666)
            if button_VOL3.collidepoint(mx, my):
                if klik:
                    pygame.mixer.music.set_volume(0.999)
            pygame.draw.rect(screen, BLUE, button_VOLuit)
            pygame.draw.rect(screen, BLUE, button_VOL1)
            pygame.draw.rect(screen, BLUE, button_VOL2)
            pygame.draw.rect(screen, BLUE, button_VOL3)

            klik = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            mainClock.tick(60)

    def sluiten():
        running = True
        while running:

            pygame.display.quit()
            pygame.quit()


    main_menu()


#connectfour_with_ai()
gui()

