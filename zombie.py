import pygame
from kaboom import Kaboom
import random
import game_setup

sound_boom = pygame.mixer.Sound("./music/cherrybomb.ogg")

class Zombie(pygame.sprite.Sprite):

    def __init__(self, *group):
        super().__init__(*group)
        self.anim = [pygame.image.load('./img/Zmb/DefZombieWalking_1.png').convert(),
                     pygame.image.load('./img/Zmb/DefZombieWalking_2.png').convert(),
                     pygame.image.load('./img/Zmb/DefZombieWalking_3.png').convert(),
                     pygame.image.load('./img/Zmb/DefZombieWalking_4.png').convert(),
                     pygame.image.load('./img/Zmb/DefZombieWalking_5.png').convert(),
                     pygame.image.load('./img/Zmb/DefZombieWalking_6.png').convert(),
                     pygame.image.load('./img/Zmb/DefZombieWalking_7.png').convert()]
        self.image = self.anim[0]
        self.rect = self.image.get_rect()
        self.speedx = 2
        self.rect.x = 2400
        self.rect.y = random.randrange(30,380)
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 180
        self.spawn_zombie = 0
        self.hp = 2

    def update(self):
        self.rect.x -= self.speedx
       
        now = pygame.time.get_ticks()
        self.image = self.anim[self.frame]
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
        if self.frame == len(self.anim):
            self.frame = 0
        if self.rect.left < 150:
            self.hp = 2
            self.spawn_zombie = 1
              
        if self.spawn_zombie == 1:
            self.death()
            self.rect.x = 1200
            self.rect.y = random.randrange(30,380)
            self.spawn_zombie = 0
        
    def death(self):
        sound_boom.play()
        kaboom = Kaboom(self.rect.centerx, self.rect.centery)
        game_setup.all_sprites.add(kaboom)
        game_setup.kabooms.add(kaboom)
