import pygame
from os import path

img_dir = path.join(path.dirname(__file__), 'img')


menu = pygame.image.load(path.join(img_dir, 'back.png'))
ship = pygame.image.load(path.join(img_dir, 'ship.png'))
hollywood = pygame.image.load(path.join(img_dir, 'hollywood.png'))
mansion = pygame.image.load(path.join(img_dir, 'mansion.png'))
heaven = pygame.image.load(path.join(img_dir, 'heaven.png'))
library = pygame.image.load(path.join(img_dir, 'library.png'))
hell = pygame.image.load(path.join(img_dir, 'hell.png'))
shadows = pygame.image.load(path.join(img_dir, 'shadows.png'))
ice = pygame.image.load(path.join(img_dir, 'ice.png'))


