from os import path

# display settings

# WIDTH = 1280
# HEIGHT = 720
WIDTH = 1920
HEIGHT = 1080

# placing elements

if HEIGHT == 1080:
    diamonds_place = (WIDTH / 6 * 4, -50)
    diamonds_text_place = (diamonds_place[0] + 325, diamonds_place[1] + 170)
    diamonds_font = 72
    questions_place = (WIDTH / 4, HEIGHT / 3)
    first_answer_place = (questions_place[0] + 75, questions_place[1] + 75)
    second_answer_place = (questions_place[0] + 75, questions_place[1] + 375)
    questions_font = 48
    logo_place = (WIDTH / 100, 10)
    notification_place = (WIDTH / 3, HEIGHT / 4)
    girl_place = (0, HEIGHT - 50)

else:
    diamonds_place = (WIDTH / 6 * 4 + 150, -30)
    diamonds_text_place = (diamonds_place[0] + 110, diamonds_place[1] + 55)
    diamonds_font = 40
    questions_place = (WIDTH / 3, HEIGHT / 3)
    first_answer_place = (questions_place[0] + 10, questions_place[1] + 25)
    second_answer_place = (questions_place[0] + 10, questions_place[1] + 135)
    questions_font = 24
    logo_place = (WIDTH / 100 + 20, 20)
    notification_place = (WIDTH // 2.5, HEIGHT / 3)
    girl_place = (0, HEIGHT - 50)

# system variables

FPS = 30
bg = 0
diamonds_score = 10
current_line = 0
low_diamonds = False
isAsked = False
isImportant = False
isBlack = False

# girls

pirate = 0
director = 0
vampire = 0
angel = 0
Sarah = 0
Loki = 0

# files

if HEIGHT == 1080:
    img_dir = path.join(path.dirname(__file__), 'img', '1920')
else:
    img_dir = path.join(path.dirname(__file__), 'img', '720')
mus_dir = path.join(path.dirname(__file__), 'sounds')
file = path.join(path.dirname(__file__), 'text', 'choises.txt')
