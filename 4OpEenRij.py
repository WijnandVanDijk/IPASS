import numpy as np
import pygame
import sys
import math
import random
import unittest

from pygame import mixer
from pygame.locals import *

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

def gui(): # de functie waar alles wat te maken heeft met de grafische interface in zit.
    mainClock = pygame.time.Clock()

    # scherm wordt geïnitialiseerd
    pygame.init()
    pygame.display.set_caption('Hogeschool Utrecht IPASS Connect Four project, Wijnand van Dijk')
    screen = pygame.display.set_mode((960, 494), 0, 32)
    font = pygame.font.SysFont(None, 20)

    # Achtergrond muziek wordt aangezet
    mixer.music.load("BackgroundMusic.wav")
    mixer.music.play(-1) # de '-1' laat de music loopen
    pygame.mixer.music.set_volume(0.10)

    def draw_text(text, font, color, surface, x, y): # zorg ervoor dat ik text kan maken
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    klik = False

    def main_menu(): # main menu wordt aangemaakt. Knopen aangemaakt en functies toegewezen.
        global event
        global klik
        while True:


            LOGO = pygame.image.load('background.png')

            screen.fill((0, 0, 0))
            screen.blit(LOGO, (338, 10))
            # button text wordt aangemaakt
            draw_text('', font, WHITE, screen, 430, 20)
            draw_text('Play', font, WHITE, screen, 90, 385)
            draw_text('Over mij', font, WHITE, screen, 263, 385)
            draw_text('Weetjes', font, WHITE, screen, 455, 385)
            draw_text('Options', font, WHITE, screen, 645, 385)
            draw_text('Quit', font, WHITE, screen, 845, 385)

            # mouse position tracking
            mx, my = pygame.mouse.get_pos()

            # buttons worden nu 'gemaakt'
            button_play = pygame.Rect(50, 400, 100, 50)
            button_overons = pygame.Rect(240, 400, 100, 50)
            button_weetjes = pygame.Rect(430, 400, 100, 50)
            button_options = pygame.Rect(620, 400, 100, 50)
            button_quit = pygame.Rect(810, 400, 100, 50)

            # functies van buttons toegewezen
            if button_play.collidepoint(mx, my):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if klik:
                        gamemode_select()
            if button_overons.collidepoint(mx, my):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if klik:
                        overons()
            if button_weetjes.collidepoint(mx, my):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if klik:
                        weetjes()
            if button_options.collidepoint(mx, my):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if klik:
                        options()
            if button_quit.collidepoint(mx, my):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if klik:
                        sluiten()

            # hier worden de buttons getekend, anders kan je ze niet zien (ze werken dan wel)
            pygame.draw.rect(screen, COLOR, button_play)
            pygame.draw.rect(screen, COLOR, button_overons)
            pygame.draw.rect(screen, COLOR, button_options)
            pygame.draw.rect(screen, COLOR, button_weetjes)
            pygame.draw.rect(screen, COLOR, button_quit)

            klik = False
            for event in pygame.event.get(): # als ESC word ingedrukt gaat het 1 pagina terug, dit geld voor alle schermen die worden aangemaakt.
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

    def overons(): # Het overons scherm aangemaakt met daarin informatie over mij als persoon.
        running = True
        global event
        global klik

        while running:
            screen.fill((0, 0, 0))
            ART = pygame.image.load('overmij.png') # plaatje toegevoegd voor opmaak.
            screen.blit(ART, (720, 270)) # locatie van plaatje toegewezen

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

            draw_text('Terug', font, WHITE, screen, 8, 25)
            mx, my = pygame.mouse.get_pos()
            button_back = pygame.Rect(0, 0, 50, 25)
            if button_back.collidepoint(mx, my):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if klik:
                        running = False
            pygame.draw.rect(screen, COLOR, button_back)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            mainClock.tick(60)

    def weetjes(): # weetjes aangemaakt waar weetjes worden weergegeven over connectfour en de geschiedenis van connectfour.
        global event
        global klik
        running = True
        while running:
            fact = pygame.image.load('fact.png') # plaatje toegevoegd voor opmaak.
            win_lose = pygame.image.load('ScreenHunter 38.jpg') # plaatje toegevoegd voor opmaak.
            screen.fill((0, 0, 0))
            screen.blit(fact, (367.5, 10)) # locatie van plaatje toegewezen
            screen.blit(win_lose, (710, 250)) # locatie van plaatje toegewezen



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

            draw_text('Terug', font, WHITE, screen, 8, 25)
            mx, my = pygame.mouse.get_pos()
            button_back = pygame.Rect(0, 0, 50, 25)
            if button_back.collidepoint(mx, my):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if klik:
                        running = False
            pygame.draw.rect(screen, COLOR, button_back)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            mainClock.tick(60)

    def options(): # options pagina aangemaakt. hier kan de speler het muziek volume en de bord grote aanpassen.
        global event
        global klik
        global aantal_rijen
        global aantal_kolommen
        global COLOR
        running = True
        while running:


            screen.fill((0, 0, 0))
            # button text wordt aangemaakt
            draw_text('Options', font, WHITE, screen, 455, 20)
            draw_text('Muziek volume:', font, WHITE, screen, 430, 100)
            draw_text('Uit', font, WHITE, screen, 470, 125)
            draw_text('1', font, WHITE, screen, 475, 175)
            draw_text('2', font, WHITE, screen, 475, 225)
            draw_text('3', font, WHITE, screen, 475, 275)
            draw_text('Bord grote:', font, WHITE, screen, 150, 100)
            draw_text('Standaard', font, WHITE, screen, 163, 125)
            draw_text('5x4', font, WHITE, screen, 183, 175)
            draw_text('6x5', font, WHITE, screen, 183, 225)
            draw_text('8x7', font, WHITE, screen, 108, 125)
            draw_text('9x7', font, WHITE, screen, 108, 175)
            draw_text('10x7', font, WHITE, screen, 254, 125)
            draw_text('8x8', font, WHITE, screen, 258, 175)
            draw_text('Verander kleur:', font, WHITE, screen, 720, 100)
            draw_text('Standaard', font, WHITE, screen, 737, 125)
            draw_text('Blauw', font, WHITE, screen, 747, 175)
            draw_text('Paars', font, WHITE, screen, 747, 225)
            draw_text('Wit', font, WHITE, screen, 682, 125)
            draw_text('Roze', font, WHITE, screen, 677, 175)
            draw_text('Groen', font, WHITE, screen, 822, 125)
            draw_text('Oranje', font, WHITE, screen, 822, 175)
            draw_text('Terug', font, WHITE, screen, 8, 25)

            # mouse position tracking
            mx, my = pygame.mouse.get_pos()

            # buttons worden nu 'gemaakt'
            button_VOLuit = pygame.Rect(455, 140, 50, 25)
            button_VOL1 = pygame.Rect(455, 190, 50, 25)
            button_VOL2= pygame.Rect(455, 240, 50, 25)
            button_VOL3 = pygame.Rect(455, 290, 50, 25)
            button_7x6 = pygame.Rect(168, 140, 50, 25)
            button_5x4 = pygame.Rect(168, 190, 50, 25)
            button_6x5 = pygame.Rect(168, 240, 50, 25)
            button_8x7 = pygame.Rect(93, 140, 50, 25)
            button_9x7 = pygame.Rect(93, 190, 50, 25)
            button_10x7 = pygame.Rect(243, 140, 50, 25)
            button_8x8 = pygame.Rect(243, 190, 50, 25)
            button_LichtBlauw = pygame.Rect(742, 140, 50, 25)
            button_Blauw = pygame.Rect(742, 190, 50, 25)
            button_Paars = pygame.Rect(742, 240, 50, 25)
            button_Wit = pygame.Rect(667, 140, 50, 25)
            button_roze = pygame.Rect(667, 190, 50, 25)
            button_groen = pygame.Rect(817, 140, 50, 25)
            button_oranje = pygame.Rect(817, 190, 50, 25)
            button_back = pygame.Rect(0, 0, 50, 25)


            # functies van buttons toegewezen
            if button_VOLuit.collidepoint(mx, my):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if klik:
                        pygame.mixer.music.set_volume(0)
            if button_VOL1.collidepoint(mx, my):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if klik:
                        pygame.mixer.music.set_volume(0.05)
            if button_VOL2.collidepoint(mx, my):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if klik:
                        pygame.mixer.music.set_volume(0.10)
            if button_VOL3.collidepoint(mx, my):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if klik:
                        pygame.mixer.music.set_volume(0.15)
            if button_7x6.collidepoint(mx, my):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if klik:
                        aantal_kolommen = 7
                        aantal_rijen = 6
            if button_5x4.collidepoint(mx, my):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if klik:
                        aantal_kolommen = 5
                        aantal_rijen = 4
            if button_6x5.collidepoint(mx, my):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if klik:
                        aantal_kolommen = 6
                        aantal_rijen = 5
            if button_8x7.collidepoint(mx, my):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if klik:
                        aantal_kolommen = 8
                        aantal_rijen = 7
            if button_9x7.collidepoint(mx, my):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if klik:
                        aantal_kolommen = 9
                        aantal_rijen = 7
            if button_10x7.collidepoint(mx, my):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if klik:
                        aantal_kolommen = 10
                        aantal_rijen = 7
            if button_8x8.collidepoint(mx, my):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if klik:
                        aantal_kolommen = 8
                        aantal_rijen = 8
            if button_LichtBlauw.collidepoint(mx, my):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if klik:
                        COLOR = LIGHT_BLUE
            if button_Blauw.collidepoint(mx, my):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if klik:
                        COLOR = BLUE
            if button_Paars.collidepoint(mx, my):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if klik:
                        COLOR = PURPLE
            if button_Wit.collidepoint(mx, my):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if klik:
                        COLOR = WHITE
            if button_groen.collidepoint(mx, my):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if klik:
                        COLOR = GREEN
            if button_oranje.collidepoint(mx, my):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if klik:
                        COLOR = ORANGE
            if button_roze.collidepoint(mx, my):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if klik:
                        COLOR = PINK
            if button_back.collidepoint(mx, my):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if klik:
                        running = False

            # hier worden de buttons getekend, anders kan je ze niet zien (ze werken dan wel)
            pygame.draw.rect(screen, COLOR, button_VOLuit)
            pygame.draw.rect(screen, COLOR, button_VOL1)
            pygame.draw.rect(screen, COLOR, button_VOL2)
            pygame.draw.rect(screen, COLOR, button_VOL3)
            pygame.draw.rect(screen, COLOR, button_7x6)
            pygame.draw.rect(screen, COLOR, button_5x4)
            pygame.draw.rect(screen, COLOR, button_6x5)
            pygame.draw.rect(screen, COLOR, button_8x7)
            pygame.draw.rect(screen, COLOR, button_9x7)
            pygame.draw.rect(screen, COLOR, button_10x7)
            pygame.draw.rect(screen, COLOR, button_8x8)
            pygame.draw.rect(screen, COLOR, button_LichtBlauw)
            pygame.draw.rect(screen, COLOR, button_Blauw)
            pygame.draw.rect(screen, COLOR, button_Paars)
            pygame.draw.rect(screen, COLOR, button_Wit)
            pygame.draw.rect(screen, COLOR, button_groen)
            pygame.draw.rect(screen, COLOR, button_oranje)
            pygame.draw.rect(screen, COLOR, button_roze)
            pygame.draw.rect(screen, COLOR, button_back)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            mainClock.tick(60)

    def sluiten(): # sluit pygame af.
        running = True
        while running:

            pygame.display.quit()
            pygame.quit()

    def gamemode_select(): # Hier kan de speler selecteren of hij tegen een vriend/ennis wilt spelen of tegen de AI
        global event
        running = True
        while running:
            screen.fill((0, 0, 0))
            klik = True

            # button text wordt aangemaakt
            draw_text('Gamemode select', font, (255, 255, 255), screen, 430, 20)
            draw_text('MENS VS MENS', font, WHITE, screen, 275, 187)
            draw_text('MENS VS AI', font, WHITE, screen, 630, 187)
            draw_text('Terug', font, WHITE, screen, 8, 25)

            # mouse position tracking
            mx, my = pygame.mouse.get_pos()

            # buttons worden nu 'gemaakt'
            button_MENSvsMENS = pygame.Rect(230, 200, 200, 100)
            button_MENSvsAI = pygame.Rect(580, 200, 200, 100)
            button_back = pygame.Rect(0, 0, 50, 25)

            # functies van buttons toegewezen
            if button_MENSvsMENS.collidepoint(mx, my):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if klik:
                        connectfour_no_ai()
            if button_MENSvsAI.collidepoint(mx, my):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if klik:
                        difficulty_select()
            if button_back.collidepoint(mx, my):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if klik:
                        running = False
            # hier worden de buttons getekend, anders kan je ze niet zien (ze werken dan wel)
            pygame.draw.rect(screen, COLOR, button_MENSvsMENS)
            pygame.draw.rect(screen, COLOR, button_MENSvsAI)
            pygame.draw.rect(screen, COLOR, button_back)


            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            mainClock.tick(60)

    def difficulty_select(): # als de speler gekozen heeft om tegen de AI te spelen kan de speler hier de moeilijkheid kiezen.
        global event
        running = True
        while running:
            screen.fill((0, 0, 0))
            difi = pygame.image.load('dificulty_banner.jpg') # plaatje toegevoegd voor opmaak.
            easy = pygame.image.load('easy.png') # plaatje toegevoegd voor opmaak.
            medium = pygame.image.load('medium.png') # plaatje toegevoegd voor opmaak.
            hard = pygame.image.load('hard.png') # plaatje toegevoegd voor opmaak.
            screen.blit(difi, (400, 25)) # locatie van plaatje toegewezen
            screen.blit(easy, (238, 227)) # locatie van plaatje toegewezen
            screen.blit(medium, (433, 230)) # locatie van plaatje toegewezen
            screen.blit(hard, (635, 230)) # locatie van plaatje toegewezen
            klik = True

            draw_text('Difficulty select', font, (255, 255, 255), screen, 430, 20)
            draw_text('Terug', font, WHITE, screen, 8, 25)

            # mouse position tracking
            mx, my = pygame.mouse.get_pos()

            # buttons worden nu 'gemaakt'
            button_easy = pygame.Rect(205, 300, 150, 75)
            button_medium = pygame.Rect(405, 300, 150, 75)
            button_hard = pygame.Rect(605, 300, 150, 75)
            button_back = pygame.Rect(0, 0, 50, 25)

            # functies van buttons toegewezen
            if button_easy.collidepoint(mx, my):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if klik:
                        connectfour_with_ai_easy()
            if button_medium.collidepoint(mx, my):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if klik:
                        connectfour_with_ai_medium()
            if button_hard.collidepoint(mx, my):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if klik:
                        connectfour_with_ai_hard()
            if button_back.collidepoint(mx, my):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if klik:
                        running = False

            # hier worden de buttons getekend, anders kan je ze niet zien (ze werken dan wel)
            pygame.draw.rect(screen, COLOR, button_easy)
            pygame.draw.rect(screen, COLOR, button_medium)
            pygame.draw.rect(screen, COLOR, button_hard)
            pygame.draw.rect(screen, COLOR, button_back)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            mainClock.tick(60)

    main_menu()



def connectfour_with_ai_hard(): # met minimax algoritme

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

        # Score diagonaal van rechts onder naar links boven
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

    def get_geldige_zet(bord): # kijkt of het een mogelijk zet is. geeft een lijst van de mogelijk locaties
        geldige_locatie = []
        for kolom in range(aantal_kolommen):
            if geldige_locatie_func(bord, kolom):
                geldige_locatie.append(kolom)

        return geldige_locatie

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

    pygame.init()  # bron voor pygame: https://www.pygame.org/docs/ref/draw.html initialiseerd Pygame

    squaresize = 100  # in pixels

    breedte = aantal_kolommen * squaresize
    hoogte = (aantal_rijen + 1) * squaresize  # +1 zodat je ziet waar je de zet doet

    size = (breedte, hoogte)

    radius = int(squaresize / 2 - 5) # -5 zodat de cirkels niet aan elkaar vast zitten, dit is esthetisch gezien beter

    Gamescherm = pygame.display.set_mode(size) # zet scherm grote goed voor pygame
    teken_bord(bord)
    pygame.display.update()

    myfont = pygame.font.SysFont('monospace', 75)

    beurd = random.randint(MENS, AI) # random keuze wie eerst mag

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
            pygame.time.wait(10000)  # in miliseconds, dus 10 seconden
            pygame.display.quit()
            pygame.quit()
            pygame.quit()



def connectfour_with_ai_medium(): # zoekt naar 3 en 4 op een rij een speelt in op de tegenstander zijn zet (soms)

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

    def winnende_zet(bord, steen): # kijkt of er een 4 op een rij is. kijkt naar alle mogelijkheden plekken waar een vier op een rij kan zijn.
        # kijkt naar alle HORIZONTALEN locaties voor een 4 op een rij.
        for k in range(aantal_kolommen - 3): # -3 omdat je bij de laatste 3 geen vier op een rij meer kan krijgen(links naar rechts).
            for r in range(aantal_rijen):
                if bord[r][k] == steen and bord[r][k + 1] == steen and bord[r][k + 2] == steen and bord[r][
                    k + 3] == steen:
                    return True

        # kijkt naar alle VERTICALEN locaties voor een 4 op een rij.
        for k in range(aantal_kolommen):
            for r in range(aantal_rijen - 3): # -3 omdat je bij de laatste 3 geen vier op een rij meer kan krijgen(beneden naar boven).
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
            kolom = kies_beste_zet(bord, AI_STEEN)

            if geldige_locatie_func(bord, kolom):
                pygame.time.wait(500) # milliseconde
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
            pygame.time.wait(10000)  # in miliseconds, dus 10 seconden
            pygame.display.quit()
            pygame.quit()
            pygame.quit()



def connectfour_with_ai_easy(): # compleet random geselecteerde kolom waar de steen geplaatst wordt

    global event
    MENS = 0
    AI = 1

    def maak_bord(): # bord wordt aangemaakt
        bord = np.zeros((aantal_rijen, aantal_kolommen))  # np.zeros maakt een matrix aan gevuld met nullen
        return bord

    def leg_steen(bord, rij, kolom, steen):  # legt de steen.
        bord[rij][kolom] = steen

    def geldige_locatie(bord, kolom):  # kijkt of de locatie geldig is voor de zet.
        return bord[aantal_rijen - 1][kolom] == 0  # kijkt of er nog minimaal 1 plek over is in de kolom.

    def volgende_open_rij(bord, kolom):  # kijkt op welke rij de steen gelegd wordt.
        for r in range(aantal_rijen):
            if bord[r][kolom] == 0:  # als de plek nog een 0 is (0=leeg) de eerste 0 wordt gereturnd.
                return r

    def print_bord(bord):  # flipt het bord zodat de stenen naar beneden 'vallen'.
        print(np.flip(bord, 0))

    def winnende_zet(bord,
                     steen):  # kijkt of er een 4 op een rij is. kijkt naar alle mogelijkheden plekken waar een vier op een rij kan zijn.
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

        # kijkt naar alle links-rechts boven locaties voor een 4 op een rij
        for k in range(aantal_kolommen - 3):
            for r in range(aantal_rijen - 3):
                if bord[r][k] == steen and bord[r + 1][k + 1] == steen and bord[r + 2][k + 2] == steen and bord[r + 3][
                    k + 3] == steen:
                    return True

        # kijkt naar alle rechts-links boven locaties voor een 4 op een rij
        for k in range(aantal_kolommen - 3):
            for r in range(3, aantal_rijen):
                if bord[r][k] == steen and bord[r - 1][k + 1] == steen and bord[r - 2][k + 2] == steen and bord[r - 3][
                    k + 3] == steen:
                    return True

    def teken_bord(bord):  # maakt het bord in PyGame.
        for k in range(aantal_kolommen):
            for r in range(aantal_rijen):
                pygame.draw.rect(Gamescherm, COLOR,
                                 (k * squaresize, r * squaresize + squaresize, squaresize, squaresize))
                pygame.draw.circle(Gamescherm, BLACK, (
                    int(k * squaresize + squaresize / 2), int(r * squaresize + squaresize + squaresize / 2)), radius)

        for k in range(aantal_kolommen):
            for r in range(aantal_rijen):
                if bord[r][k] == 1:  # wie aan de beurd is, in dit geval speler 1.
                    pygame.draw.circle(Gamescherm, RED, (
                        int(k * squaresize + squaresize / 2), hoogte - int(r * squaresize + squaresize / 2)), radius)
                elif bord[r][k] == 2:  # wie aan de beurd is, in dit geval speler 2.
                    pygame.draw.circle(Gamescherm, YELLOW, (
                        int(k * squaresize + squaresize / 2), hoogte - int(r * squaresize + squaresize / 2)), radius)
        pygame.display.update()

    bord = maak_bord()
    print_bord(bord)
    game_over = False  # zodat de main game loop kan blijven lopen, het wordt alleen True als iemand 4 vier op een rij heeft.
    beurd = 0

    pygame.init()  # bron voor pygame: https://www.pygame.org/docs/ref/draw.html

    squaresize = 100  # in pixels

    breedte = aantal_kolommen * squaresize
    hoogte = (aantal_rijen + 1) * squaresize  # +1 zodat je ziet waar je de zet doet

    size = (breedte, hoogte)

    radius = int(squaresize / 2 - 5)  # zorgt ervoor dat de cirkels niet aanraken.

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
                posx = event.pos[0]  # positie van muis.
                if beurd == MENS:
                    pygame.draw.circle(Gamescherm, RED, (posx, int(squaresize / 2)), radius)
                else:
                    pygame.draw.circle(Gamescherm, YELLOW, (posx, int(squaresize / 2)), radius)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(Gamescherm, BLACK, (0, 0, breedte, squaresize))
                if beurd == 0:
                    posx = event.pos[0]  # positie van muis.
                    kolom = int(math.floor(posx / squaresize))

                    if geldige_locatie(bord, kolom):
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

            kolom = random.randint(0, aantal_kolommen - 1)

            if geldige_locatie(bord, kolom):
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
            pygame.time.wait(10000)  # in miliseconds, dus 10 seconden
            pygame.display.quit()
            pygame.quit()



def connectfour_no_ai(): # Mens tegen mens.

    def maak_bord(): # bord wordt aangemaakt
        bord = np.zeros((aantal_rijen, aantal_kolommen))  # np.zeros maakt een matrix aan gevuld met nullen.
        return bord

    def leg_steen(bord, rij, kolom, steen): # legt de steen.
        bord[rij][kolom] = steen

    def geldige_locatie(bord, kolom): # kijkt of de locatie geldig is voor de zet.
        return bord[aantal_rijen - 1][kolom] == 0 # kijkt of er nog minimaal 1 plek over is in de kolom.

    def volgende_open_rij(bord, kolom): # kijkt op welke rij de steen gelegd wordt.
        for r in range(aantal_rijen):
            if bord[r][kolom] == 0: # als de plek nog een 0 is (0=leeg) de eerste 0 wordt gereturnd.
                return r

    def print_bord(bord): # flipt het bord zodat de stenen naar beneden 'vallen'.
        print(np.flip(bord, 0))

    def winnende_zet(bord, steen): # kijkt of er een 4 op een rij is. kijkt naar alle mogelijkheden plekken waar een vier op een rij kan zijn.
        # kijkt naar alle HORIZONTALEN locaties voor een 4 op een rij.
        for k in range(aantal_kolommen - 3): # -3 omdat je bij de laatste 3 geen vier op een rij meer kan krijgen(links naar rechts).
            for r in range(aantal_rijen):
                if bord[r][k] == steen and bord[r][k + 1] == steen and bord[r][k + 2] == steen and bord[r][
                    k + 3] == steen:
                    return True

        # kijkt naar alle VERTICALEN locaties voor een 4 op een rij.
        for k in range(aantal_kolommen):
            for r in range(aantal_rijen - 3): # -3 omdat je bij de laatste 3 geen vier op een rij meer kan krijgen(beneden naar boven).
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
    game_over = False # zodat de main game loop kan blijven lopen, het wordt alleen True als iemand 4 vier op een rij heeft.
    beurd = 0

    pygame.init()  # bron voor pygame: https://www.pygame.org/docs/ref/draw.html

    squaresize = 100  # in pixels

    breedte = aantal_kolommen * squaresize
    hoogte = (aantal_rijen + 1) * squaresize  # +1 zodat je ziet waar je de zet doet.

    size = (breedte, hoogte)

    radius = int(squaresize / 2 - 5) # zorgt ervoor dat de cirkels niet aanraken.

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
                posx = event.pos[0] # positie van muis.
                if beurd == 0:
                    pygame.draw.circle(Gamescherm, RED, (posx, int(squaresize / 2)), radius)
                else:
                    pygame.draw.circle(Gamescherm, YELLOW, (posx, int(squaresize / 2)), radius)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(Gamescherm, BLACK, (0, 0, breedte, squaresize))
                if beurd == 0:
                    posx = event.pos[0] # positie van muis.
                    kolom = int(math.floor(posx / squaresize))

                    if geldige_locatie(bord, kolom):
                        rij = volgende_open_rij(bord, kolom)
                        leg_steen(bord, rij, kolom, 1)

                        if winnende_zet(bord, 1):
                            label = myfont.render("Speler 1 wint!", 1, RED)
                            Gamescherm.blit(label, (40, 10))
                            game_over = True

                else:
                    posx = event.pos[0] # positie van muis.
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
                    pygame.time.wait(10000)  # in miliseconds, dus 10 seconden.
                    pygame.display.quit()
                    pygame.quit()



gui()


