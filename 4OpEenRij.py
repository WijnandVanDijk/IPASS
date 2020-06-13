import numpy as np
import pygame
import sys
import math
from pygame.locals import *


def connectfour():

    PURPLE = (75, 0, 130)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)

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
        for k in range(aantal_kolommen - 3):
            for r in range(aantal_rijen):
                if bord[r][k] == steen and bord[r][k + 1] == steen and bord[r][k + 2] == steen and bord[r][k + 3] == steen:
                    return True

        for k in range(aantal_kolommen):
            for r in range(aantal_rijen - 3):
                if bord[r][k] == steen and bord[r + 1][k] == steen and bord[r + 2][k] == steen and bord[r + 3][k] == steen:
                    return True

        for k in range(aantal_kolommen - 3):
            for r in range(aantal_rijen - 3):
                if bord[r][k] == steen and bord[r + 1][k + 1] == steen and bord[r + 2][k + 2] == steen and bord[r + 3][k + 3] == steen:
                    return True

        for k in range(aantal_kolommen - 3):
            for r in range(3, aantal_rijen):
                if bord[r][k] == steen and bord[r - 1][k + 1] == steen and bord[r - 2][k + 2] == steen and bord[r - 3][k + 3] == steen:
                    return True

    def teken_bord(bord):
        for k in range(aantal_kolommen):
            for r in range(aantal_rijen):
                pygame.draw.rect(Gamescherm, PURPLE, (k * squaresize, r * squaresize+squaresize, squaresize, squaresize))
                pygame.draw.circle(Gamescherm, BLACK, (int(k * squaresize + squaresize/2), int(r * squaresize + squaresize + squaresize/2)), radius)

        for k in range(aantal_kolommen):
            for r in range(aantal_rijen):
                if bord[r][k] == 1:
                    pygame.draw.circle(Gamescherm, RED, (int(k * squaresize + squaresize / 2), hoogte - int(r * squaresize + squaresize / 2)), radius)
                elif bord[r][k] == 2:
                    pygame.draw.circle(Gamescherm, YELLOW, (int(k * squaresize + squaresize / 2), hoogte - int(r * squaresize + squaresize / 2)), radius)
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
                    kolom = int(math.floor(posx/squaresize))

                    if geldige_locatie(bord, kolom):
                        rij = volgende_open_rij(bord, kolom)
                        leg_steen(bord, rij, kolom, 1)

                        if winnende_zet(bord, 1):
                            label = myfont.render("Speler 1 wint!", 1, RED)
                            Gamescherm.blit(label, (40, 10))
                            game_over = True

                else:
                    posx = event.pos[0]
                    kolom = int(math.floor(posx/squaresize))

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
    pygame.display.set_caption('game base')
    screen = pygame.display.set_mode((960, 494), 0, 32)

    font = pygame.font.SysFont(None, 20)

    def draw_text(text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    click = False

    def main_menu():
        while True:

            screen.fill((0, 0, 0))
            draw_text('Connect Four', font, (255, 255, 255), screen, 430, 20)
            draw_text('Play', font, (255, 255, 255), screen, 90, 385)
            draw_text('Over ons', font, (255, 255, 255), screen, 263, 385)
            draw_text('Weetjes', font, (255, 255, 255), screen, 455, 385)
            draw_text('Options', font, (255, 255, 255), screen, 645, 385)
            draw_text('Quit', font, (255, 255, 255), screen, 845, 385)

            mx, my = pygame.mouse.get_pos()

            button_play = pygame.Rect(50, 400, 100, 50)
            button_overons = pygame.Rect(240, 400, 100, 50)
            button_weetjes = pygame.Rect(430, 400, 100, 50)
            button_options = pygame.Rect(620, 400, 100, 50)
            button_quit = pygame.Rect(810, 400, 100, 50)
            if button_play.collidepoint((mx, my)):
                if click:
                    connectfour()
            if button_overons.collidepoint((mx, my)):
                if click:
                    overons()
            if button_weetjes.collidepoint((mx, my)):
                if click:
                    weetjes()
            if button_options.collidepoint((mx, my)):
                if click:
                    options()
            if button_quit.collidepoint((mx, my)):
                if click:
                    quit()
            pygame.draw.rect(screen, (75, 0, 130), button_play)
            pygame.draw.rect(screen, (75, 0, 130), button_overons)
            pygame.draw.rect(screen, (75, 0, 130), button_options)
            pygame.draw.rect(screen, (75, 0, 130), button_weetjes)
            pygame.draw.rect(screen, (75, 0, 130), button_quit)

            click = False
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
                        click = True

            pygame.display.update()
            mainClock.tick(60)

    def overons():
        running = True
        while running:
            screen.fill((0, 0, 0))

            draw_text('Over ons', font, (255, 255, 255), screen, 430, 20)
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
            screen.fill((0, 0, 0))

            draw_text('Weetjes', font, (255, 255, 255), screen, 430, 20)
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
        running = True
        while running:
            screen.fill((0, 0, 0))

            draw_text('Options', font, (255, 255, 255), screen, 430, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            mainClock.tick(60)

    def quit():
        running = True
        while running:
            screen.fill((0, 0, 0))

            pygame.display.quit()
            pygame.quit()



    main_menu()

gui()