import pygame
import sys
import time

from config import *
import back
import colors
import reader


def girlFinder():
    global pirate, director, vampire, angel, Sarah, Loki, notification_girl, show_girl
    girl = ''
    max_point = max(pirate, director, vampire, angel, Sarah, Loki)
    if max_point <= 0 or (pirate, director, vampire, angel, Sarah, Loki).count(max_point) > 1:
        girl = 'Алексей'
    else:
        if pirate == max_point:
            girl = 'Пиратка'
            notification_girl = pygame.image.load(path.join(img_dir, 'notification_pirate.png'))
        elif director == max_point:
            girl = 'Режиссерка'
            notification_girl = pygame.image.load(path.join(img_dir, 'notification_director.png'))
        elif vampire == max_point:
            girl = 'Вампирша'
            notification_girl = pygame.image.load(path.join(img_dir, 'notification_vampire.png'))
        elif angel == max_point:
            girl = 'Ангел'
            notification_girl = pygame.image.load(path.join(img_dir, 'notification_angel.png'))
        elif Sarah == max_point:
            girl = 'Сара/Клэр'
            notification_girl = pygame.image.load(path.join(img_dir, 'notification_sarah.png'))
        elif Loki == max_point:
            girl = 'Локи'
            notification_girl = pygame.image.load(path.join(img_dir, 'notification_loki.png'))

    print('ok', girl)
    show_girl = True
    showImportance()
    # d = pygame.font.SysFont('serif', 24)
    # d_text = d.render(str(girl), True, colors.BLACK)
    # main_surface.blit(d_text, girl_place)
    # screen.blit(main_surface, (0, 0))


def setPoints(line, number):
    global pirate, director, vampire, angel, Sarah, Loki

    if number == 1:
        if line[3] == '+':
            pirate += 1
        elif line[3] == '-':
            pirate -= 1

        if line[4] == '+':
            director += 1
        elif line[4] == '-':
            director -= 1

        if line[5] == '+':
            vampire += 1
        elif line[5] == '-':
            vampire -= 1

        if line[6] == '+':
            angel += 1
        elif line[6] == '-':
            angel -= 1

        if line[7] == '+':
            Sarah += 1
        elif line[7] == '-':
            Sarah -= 1

        if line[8] == '+':
            Loki += 1
        elif line[8] == '-':
            Loki -= 1

    else:
        if line[9] == '+':
            pirate += 1
        elif line[9] == '-':
            pirate -= 1

        if line[10] == '+':
            director += 1
        elif line[10] == '-':
            director -= 1

        if line[11] == '+':
            vampire += 1
        elif line[11] == '-':
            vampire -= 1

        if line[12] == '+':
            angel += 1
        elif line[12] == '-':
            angel -= 1

        if line[13] == '+':
            Sarah += 1
        elif line[13] == '-':
            Sarah -= 1

        if line[14] == '+':
            Loki += 1
        elif line[14] == '-':
            Loki -= 1

    print(pirate, director, vampire, angel, Sarah, Loki)


def showImportance():
    alpha = 0
    while alpha < 255:
        alpha += 80
        pygame.display.flip()
        showScreen(alpha)
    time.sleep(2)
    while alpha > 0:
        alpha -= 80
        pygame.display.flip()
        showScreen(alpha)


def getLine(number):
    lines = reader.readText()
    lines = lines.splitlines()[number].split(';')
    return lines


def getFinal():
    line = reader.readFinal()
    line = line.split(';')
    print(line)
    return line


def getQuestion(number=0, dontGiveAFuck=False):
    global isAsked, show_final
    # print(line)
    if show_final:
        if diamonds_score < 30:
            cloud = pygame.image.load(path.join(img_dir, 'cloud_final_bad.png'))
        else:
            cloud = pygame.image.load(path.join(img_dir, 'cloud_final.png'))
        line = getFinal()
    elif diamonds_score >= 5 or dontGiveAFuck:
        cloud = pygame.image.load(path.join(img_dir, 'cloud.png'))
        line = getLine(number)
    elif diamonds_score < 5:
        cloud = pygame.image.load(path.join(img_dir, 'cloud_bad.png'))
        global low_diamonds
        low_diamonds = True
        line = getLine(number)
    d = pygame.font.SysFont('serif', questions_font)
    d_1 = d.render(line[0], True, colors.WHITE)
    d_2 = d.render(line[1], True, colors.WHITE)
    screen.blit(cloud, questions_place)
    screen.blit(d_1, first_answer_place)
    screen.blit(d_2, second_answer_place)
    global isImportant
    isImportant = bool(line[2])
    return line


def makeItShiny(coordinates):
    screen.blit(shine, coordinates)
    if first:
        getQuestion(current_line, True)
    else:
        getQuestion(current_line)
    pygame.display.flip()
    time.sleep(2)
    showScreen()


def addDiamonds():
    global diamonds_score
    diamonds_score += 5
    showScreen()
    diamonds_print(diamonds_score)


def removeDiamonds(amount=5):
    global diamonds_score
    diamonds_score -= amount
    showScreen()
    diamonds_print(diamonds_score)


def showScreen(alpha=0):
    screen.blit(background_surface, (0, 0))
    main_surface.blit(main_surface, (0, 0))
    main_surface.blit(background, (0, 0))
    main_surface.blit(diamonds, diamonds_place)
    main_surface.blit(logo, logo_place)
    if show_girl:
        notification.set_alpha(0)
        notification_girl.set_alpha(alpha)
        notification_low.set_alpha(0)
    elif low_diamonds:
        notification.set_alpha(0)
        notification_girl.set_alpha(0)
        notification_low.set_alpha(alpha)
    else:
        notification.set_alpha(alpha)
        notification_girl.set_alpha(0)
        notification_low.set_alpha(0)
    main_surface.blit(notification, notification_place)
    main_surface.blit(notification_low, notification_place)
    main_surface.blit(notification_girl, notification_place)
    diamonds_print(diamonds_score)
    screen.blit(main_surface, (0, 0))


def diamonds_print(score):
    d = pygame.font.SysFont('serif', diamonds_font)
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
        clock.tick(FPS)
    background = back.backgrounds[number]
    while alpha < 255:
        alpha += 30
        main_surface.set_alpha(alpha)
        pygame.display.flip()
        showScreen()
        clock.tick(FPS)


def fadeToBlack():
    global isBlack
    if not isBlack:
        alpha = 255
        main_surface.set_alpha(alpha)
        while alpha > 0:
            alpha -= 30
            main_surface.set_alpha(alpha)
            pygame.display.flip()
            showScreen()
            clock.tick(FPS)
            isBlack = True
    else:
        alpha = 0
        while alpha < 255:
            alpha += 30
            main_surface.set_alpha(alpha)
            pygame.display.flip()
            showScreen()
            clock.tick(FPS)
            isBlack = False


def changeBG(number):
    global background
    background = back.backgrounds[number]


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pyRomance v0.1")
clock = pygame.time.Clock()

background_surface = pygame.Surface(screen.get_size())
background_surface.fill(colors.BLACK)
main_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
background = back.backgrounds[0]
diamonds = pygame.image.load(path.join(img_dir, 'diamond_bar.png'))
logo = pygame.image.load(path.join(img_dir, 'logo.png'))
notification = pygame.image.load(path.join(img_dir, 'notification.png'))
notification_low = pygame.image.load(path.join(img_dir, 'notification_low.png'))
notification_girl = pygame.image.load(path.join(img_dir, 'notification_girl.png'))
shine = pygame.image.load(path.join(img_dir, 'shine.png'))
# diamonds_sound = pygame.mixer.Sound(path.join(mus_dir, 'diamond.mp3'))
# check_sound = pygame.mixer.Sound(path.join(mus_dir, 'check.mp3'))

showScreen()

running = True

while running:
    for event in pygame.event.get():

        # exit

        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:

            # exit too

            if event.key == pygame.K_ESCAPE:
                sys.exit()

            # changing backs

            elif event.key == pygame.K_UP:
                if bg < len(back.backgrounds) - 1:
                    bg += 1
                    bgchanger(bg)
                    isAsked = False
                else:
                    bg = 0
                    bgchanger(bg)
                    isAsked = False
            elif event.key == pygame.K_DOWN:
                if bg > 0:
                    bg -= 1
                    bgchanger(bg)

            # final question

            elif event.key == pygame.K_e:
                isAsked = False
                show_final = True
                print(show_final)
                getQuestion()

            # removing and adding diamonds

            elif event.key == pygame.K_w:
                addDiamonds()
                isAsked = False
                if diamonds_score >= 5:
                    low_diamonds = False

            elif event.key == pygame.K_s:
                removeDiamonds()
                isAsked = False
                if diamonds_score < 5:
                    low_diamonds = True

            # get next question

            elif event.key == pygame.K_SPACE:
                if current_line < 10:
                    isAsked = True
                    getQuestion(current_line)

            # choosing answers

            elif event.key == pygame.K_1:
                if isAsked:
                    if not low_diamonds:
                        setPoints(getLine(current_line), 1)
                        # diamonds_sound.play()
                        removeDiamonds()
                        first = True
                        makeItShiny(shine_first_answer)
                        showScreen()
                        isAsked = False
                        current_line += 1
                    else:
                        setPoints(getLine(current_line), 2)
                        # check_sound.play()
                        showScreen()
                        isAsked = False
                        first = False
                        makeItShiny(shine_second_answer)
                        showImportance()
                        low_diamonds = False
                        current_line += 1
                    if isImportant:
                        # print(isImportant)
                        showImportance()
                elif show_final:
                    removeDiamonds(30)
                    showScreen()
            elif event.key == pygame.K_2:
                if isAsked:
                    setPoints(getLine(current_line), 2)
                    low_diamonds = False
                    # check_sound.play()
                    showScreen()
                    isAsked = False
                    first = False
                    makeItShiny(shine_second_answer)
                    if isImportant:
                        # print(isImportant)
                        showImportance()
                    current_line += 1
                elif show_final:
                    removeDiamonds(30)
                    showScreen()

            # refresh screen

            elif event.key == pygame.K_r:
                showScreen()
                isAsked = False

            # find ur dream gf

            elif event.key == pygame.K_f:
                girlFinder()
                show_girl = True

            # fade to black

            elif event.key == pygame.K_q:
                fadeToBlack()

            # changing back while in fade

            elif event.key == pygame.K_a:
                if isBlack:
                    bg += 1
                    changeBG(bg)
            elif event.key == pygame.K_z:
                if isBlack:
                    bg -= 1
                    changeBG(bg)

            # delete occasional girl-finder and final-shower flags

            elif event.key == pygame.K_DELETE:
                show_girl = False
                show_final = False
                showScreen()

    clock.tick(FPS)
    pygame.display.update()
