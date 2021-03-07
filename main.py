import pygame
import sys
from os import path
import colors
import reader


def getLine(number):
    lines = reader.nextLine()
    lines = lines.splitlines()[number].split(';')
    return lines


def getQuestion(number):
    global isAsked
    isAsked = True
    line = getLine(number)
    print(line)
    cloud = pygame.image.load(path.join(img_dir, 'cloud.png'))
    d = pygame.font.SysFont('serif', 48)
    d_1 = d.render(line[0], True, colors.BLACK)
    d_2 = d.render(line[1], True, colors.BLACK)
    screen.blit(cloud, questions_place)
    screen.blit(d_1, (questions_place[0] + 855, questions_place[1] + 325))
    screen.blit(d_2, (questions_place[0] + 220, questions_place[1] + 120))


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


def showScreen():
    screen.blit(background, (0, 0))
    screen.blit(diamonds, diamonds_place)
    screen.blit(logo, logo_place)
    diamonds_print(diamonds_score)


def diamonds_print(score):
    d = pygame.font.SysFont('serif', 72)
    d_text = d.render(str(score), True, colors.WHITE)
    screen.blit(d_text, diamonds_text_place)


def bgchanger(number):
    global background
    if number == 1:
        background = pygame.image.load(path.join(img_dir, 'ship.png'))
    elif number == 2:
        background = pygame.image.load(path.join(img_dir, 'hollywood.png'))
    elif number == 3:
        background = pygame.image.load(path.join(img_dir, 'mansion.png'))
    elif number == 4:
        background = pygame.image.load(path.join(img_dir, 'heaven.png'))
    elif number == 5:
        background = pygame.image.load(path.join(img_dir, 'library.png'))
    elif number == 6:
        background = pygame.image.load(path.join(img_dir, 'hell.png'))
    elif number == 7:
        background = pygame.image.load(path.join(img_dir, 'shadows.png'))
    elif number == 8:
        background = pygame.image.load(path.join(img_dir, 'ice.png'))
    else:
        background = pygame.image.load(path.join(img_dir, 'back.png'))
    showScreen()


WIDTH = 1920
HEIGHT = 1080
diamonds_place = (WIDTH / 6 * 4, -50)
diamonds_text_place = (diamonds_place[0] + 325, diamonds_place[1] + 170)
questions_place = (WIDTH / 8, HEIGHT / 3)
logo_place = (WIDTH / 100, 10)
bg = 0
diamonds_score = 10
current_line = 0
isAsked = False

img_dir = path.join(path.dirname(__file__), 'img')
mus_dir = path.join(path.dirname(__file__), 'sounds')

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pyRomance v0.1")

background = pygame.image.load(path.join(img_dir, 'back.png'))
diamonds = pygame.image.load(path.join(img_dir, 'diamond_bar.png'))
logo = pygame.image.load(path.join(img_dir, 'logo.png'))
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
                if bg < 9:
                    bg += 1
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
                    current_line += 1
                    diamonds_sound.play()
                    removeDiamonds()
                    showScreen()
                    isAsked = False
            elif event.key == pygame.K_2:
                if isAsked:
                    current_line += 1
                    check_sound.play()
                    showScreen()
                    isAsked = False
    pygame.display.update()
