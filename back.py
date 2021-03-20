import pygame
from os import path
from config import WIDTH

import config

menu = pygame.image.load(path.join(config.img_dir, 'back.png'))
ship = pygame.image.load(path.join(config.img_dir, 'ship.png'))
hollywood = pygame.image.load(path.join(config.img_dir, 'hollywood.png'))
mansion = pygame.image.load(path.join(config.img_dir, 'mansion.png'))
heaven = pygame.image.load(path.join(config.img_dir, 'heaven.png'))
library = pygame.image.load(path.join(config.img_dir, 'library.png'))
hell = pygame.image.load(path.join(config.img_dir, 'hell.png'))
shadows = pygame.image.load(path.join(config.img_dir, 'shadows.png'))
ice = pygame.image.load(path.join(config.img_dir, 'ice.png'))

backgrounds = (menu, ship, hollywood, mansion, heaven,
               library, hell, shadows, ice)
