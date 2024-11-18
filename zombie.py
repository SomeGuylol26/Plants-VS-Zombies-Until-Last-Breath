import pygame
import random
import game_setup


class Zombie(pygame.sprite.Sprite):

    def __init__(self, *group):
        super().__init__(*group)
        self.anim = [pygame.image.load('./img/DefZombieWalking_1.png'),
                     pygame.image.load('./img/DefZombieWalking_2.png'),
                     pygame.image.load('./img/DefZombieWalking_3.png'),
                     pygame.image.load('./img/DefZombieWalking_4.png'),
                     pygame.image.load('./img/DefZombieWalking_5.png'),
                     pygame.image.load('./img/DefZombieWalking_6.png'),
                     pygame.image.load('./img/DefZombieWalking_7.png')]
        self.image = self.anim[0]
        self.rect = self.image.get_rect()
        self.speedx = random.randrange(1,8)
        self.rect.x = 1200
        self.rect.y = random.randrange(50,450)
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 150
        self.spawn_zombie = 100
    def update(self):
        self.spawn_zombie -= 1
        self.rect.x -= self.speedx
       
        now = pygame.time.get_ticks()
        self.image = self.anim[self.frame]
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
        if self.frame == len(self.anim):
            self.frame = 0
        if self.spawn_zombie < 0:
            zombie = Zombie()
            game_setup.all_sprites.add(zombie)
            game_setup.zombies.add(zombie)
            self.spawn_zombie = 100
        if self.rect.left < -100:
            self.kill()


