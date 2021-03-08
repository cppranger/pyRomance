import pygame
import sys
from os import path
import time

import back
import colors
import reader


def showImportance():
    alpha = 0
    while alpha < 255:
        alpha += 80
        pygame.display.flip()
        showScreen(alpha)
    time.sleep(1.5)
    while alpha > 0:
        alpha -= 80
        pygame.display.flip()
        showScreen(alpha)


def getLine(number):
    lines = reader.nextLine()
    lines = lines.splitlines()[number].split(';')
    return lines


def getQuestion(number):
    global isAsked
    isAsked = True
    line = getLine(number)
    print(line)
    if diamonds_score >= 5:
        cloud = pygame.image.load(path.join(img_dir, 'cloud.png'))
    else:
        cloud = pygame.image.load(path.join(img_dir, 'cloud_bad.png'))
        global low_diamonds
        low_diamonds = True
    d = pygame.font.SysFont('serif', 48)
    d_1 = d.render(line[0], True, colors.WHITE)
    d_2 = d.render(line[1], True, colors.WHITE)
    screen.blit(cloud, questions_place)
    screen.blit(d_1, (questions_place[0] + 75, questions_place[1] + 75))
    screen.blit(d_2, (questions_place[0] + 75, questions_place[1] + 375))
    global isImportant
    isImportant = bool(line[2])


def addDiamonds():
    global diamonds_score
    diamonds_score += 5
    showScreen()
    diamonds_print(diamonds_score)


def removeDiamonds():
    global diamonds_score
    diamonds_score -= 5
    showScreen()
    diamonds_print(diamonds_score)


def showScreen(alpha=0):
    screen.blit(background_surface, (0, 0))

    main_surface.blit(main_surface, (0, 0))
    main_surface.blit(background, (0, 0))
    main_surface.blit(diamonds, diamonds_place)
    main_surface.blit(logo, logo_place)
    if not low_diamonds:
        notification.set_alpha(alpha)
        notification_low.set_alpha(0)

    else:
        notification.set_alpha(0)
        notification_low.set_alpha(alpha)
    main_surface.blit(notification, notification_place)
    main_surface.blit(notification_low, notification_place)
    diamonds_print(diamonds_score)
    screen.blit(main_surface, (0, 0))


def diamonds_print(score):
    d = pygame.font.SysFont('serif', 72)
    d_text = d.render(str(score), True, colors.WHITE)
    main_surface.blit(d_text, diamonds_text_place)


def bgchanger(number):
    global background
    alpha = 255
    main_surface.set_alpha(alpha)
    while alpha > 0:
        alpha -= 30
        main_surface.set_alpha(alpha)
        pygame.display.flip()
        showScreen()
    background = backgrounds[number]
    while alpha < 255:
        alpha += 30
        main_surface.set_alpha(alpha)
        pygame.display.flip()
        showScreen()


WIDTH = 1920
HEIGHT = 1080
diamonds_place = (WIDTH / 6 * 4, -50)
diamonds_text_place = (diamonds_place[0] + 325, diamonds_place[1] + 170)
questions_place = (WIDTH / 4, HEIGHT / 3)
logo_place = (WIDTH / 100, 10)
notification_place = (WIDTH / 3, HEIGHT / 4)
bg = 0
diamonds_score = 10
low_diamonds = False
current_line = 0
isAsked = False
isImportant = False
backgrounds = (back.menu, back.ship, back.hollywood, back.mansion, back.heaven,
               back.library, back.hell, back.shadows, back.ice)

img_dir = path.join(path.dirname(__file__), 'img')
mus_dir = path.join(path.dirname(__file__), 'sounds')

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pyRomance v0.1")

background_surface = pygame.Surface(screen.get_size())
background_surface.fill(colors.BLACK)
main_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
background = backgrounds[0]
diamonds = pygame.image.load(path.join(img_dir, 'diamond_bar.png'))
logo = pygame.image.load(path.join(img_dir, 'logo.png'))
notification = pygame.image.load(path.join(img_dir, 'notification.png'))
notification_low = pygame.image.load(path.join(img_dir, 'notification_low.png'))
diamonds_sound = pygame.mixer.Sound(path.join(mus_dir, 'diamond.mp3'))
check_sound = pygame.mixer.Sound(path.join(mus_dir, 'check.mp3'))

showScreen()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_UP:
                if bg < 8:
                    bg += 1
                    bgchanger(bg)
                else:
                    bg = 0
                    bgchanger(bg)
            elif event.key == pygame.K_DOWN:
                if bg > 0:
                    bg -= 1
                    bgchanger(bg)
            elif event.key == pygame.K_w:
                addDiamonds()
            elif event.key == pygame.K_s:
                removeDiamonds()
            elif event.key == pygame.K_SPACE:
                if current_line < 10:
                    isAsked = True
                    getQuestion(current_line)
            elif event.key == pygame.K_1:
                if isAsked:
                    if not low_diamonds:
                        current_line += 1
                        diamonds_sound.play()
                        removeDiamonds()
                        showScreen()
                        isAsked = False

                    else:
                        current_line += 1
                        check_sound.play()
                        showScreen()
                        isAsked = False
                        showImportance()
                        low_diamonds = False

                    if isImportant:
                        print(isImportant)
                        showImportance()

            elif event.key == pygame.K_2:
                if isAsked:
                    current_line += 1
                    low_diamonds = False
                    check_sound.play()
                    showScreen()
                    isAsked = False
                    if isImportant:
                        print(isImportant)
                        showImportance()
            elif event.key == pygame.K_r:
                showScreen()
    pygame.display.update()
