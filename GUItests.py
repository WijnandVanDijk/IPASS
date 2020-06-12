# start code: https://www.youtube.com/watch?v=0RryiSjpJn0&list=PLhx8v4mr6oU_NC6iNisG_ZF3UBvhhJLU8&index=10&t=01s
import pygame
import sys


mainClock = pygame.time.Clock()
from pygame.locals import *

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
                game()
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
        pygame.draw.rect(screen, (138, 43, 226), button_play)
        pygame.draw.rect(screen, (138, 43, 226), button_overons)
        pygame.draw.rect(screen, (138, 43, 226), button_options)
        pygame.draw.rect(screen, (138, 43, 226), button_weetjes)
        pygame.draw.rect(screen, (138, 43, 226), button_quit)


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


def game():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('game', font, (255, 255, 255), screen, 430, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


def overons():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('over ons', font, (255, 255, 255), screen, 430, 20)
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

        draw_text('weetjes', font, (255, 255, 255), screen, 430, 20)
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

        draw_text('options', font, (255, 255, 255), screen, 430, 20)
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

        draw_text('quit', font, (255, 255, 255), screen, 430, 20)
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