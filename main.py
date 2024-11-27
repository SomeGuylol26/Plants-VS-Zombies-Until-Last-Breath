import pygame

import game_setup
from peashooter import Peashooter
from zombie import Zombie

pygame.init()
WIDTH = 1000
HEIGHT = 514
FPS = 60
win = pygame.display.set_mode((WIDTH, HEIGHT))
img = pygame.image.load('./img/BackgroundDay.png')
clock = pygame.time.Clock()
pygame.display.set_caption('Plants VS Zombies: Until Last Breath')
pygame.mixer.music.load('./music/Music.mp3')
pygame.mixer.music.play(-1)


# Используем группы и объекты из game_setup
all_sprites = game_setup.all_sprites
peas = game_setup.peas
zombie = Zombie()
zombies = game_setup.zombies
peashooter_instance = Peashooter()
all_sprites.add(peashooter_instance)
all_sprites.add(zombie)
zombies.add(zombie)

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    all_sprites.update()
    hits = pygame.sprite.groupcollide(zombies, peas, True, True)
    for hit in hits:
        zombie = Zombie()
        all_sprites.add(zombie)
        zombies.add(zombie)
    win.blit(img, (0,0))
    all_sprites.draw(win)

    pygame.display.update()