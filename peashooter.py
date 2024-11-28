import pygame
from pea import Pea
import game_setup


sound_throw = pygame.mixer.Sound("./music/throw.ogg")
class Peashooter(pygame.sprite.Sprite):

    def __init__(self, *group):
        super().__init__(*group)
        self.anim = [pygame.image.load('./img/PeashooterIdle_1.png'),
                     pygame.image.load('./img/PeashooterIdle_2.png'),
                     pygame.image.load('./img/PeashooterIdle_3.png'),
                     pygame.image.load('./img/PeashooterIdle_4.png'),
                     pygame.image.load('./img/PeashooterIdle_5.png'),
                     pygame.image.load('./img/PeashooterIdle_6.png'),
                     pygame.image.load('./img/PeashooterIdle_7.png'),
                     pygame.image.load('./img/PeashooterIdle_8.png')]

        self.animShoot = [pygame.image.load('./img/PeashooterShoot_1.png'),
                          pygame.image.load('./img/PeashooterShoot_1.png'),
                          pygame.image.load('./img/PeashooterShoot_2.png'),
                          pygame.image.load('./img/PeashooterShoot_2.png'),
                          pygame.image.load('./img/PeashooterShoot_3.png'),
                          pygame.image.load('./img/PeashooterShoot_3.png'),
                          pygame.image.load('./img/PeashooterShoot_3.png'),
                          pygame.image.load('./img/PeashooterShoot_3.png')]
                          
        self.image = self.anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = (1000/2, 514/2)
        self.speedx = 0
        self.speedy = 0
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 150
        self.shoot_count = 0
        self.shootPlayer = False

    def update(self):
        self.shoot_count -= 1
        now = pygame.time.get_ticks()
        
        self.speedx = 0
        self.speedy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speedx -= 7
        if keys[pygame.K_RIGHT]:
            self.speedx += 7
        self.rect.x += self.speedx
        if keys[pygame.K_UP]:
            self.speedy -= 7
        if keys[pygame.K_DOWN]:
            self.speedy += 7
        self.rect.y += self.speedy
        if keys[pygame.K_SPACE] and self.shoot_count < 1:
            self.shoot_count = 60
            self.shootPlayer = True
            self.frame = 0
        if self.shootPlayer == False:
            self.frame_rate = 150
            self.image = self.anim[self.frame]
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.frame += 1
            if self.frame == len(self.anim):
                self.frame = 0
        else:
            self.frame_rate = 50
            self.image = self.animShoot[self.frame]
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.frame += 1
            if self.frame == 4:
                sound_throw.play()
                self.frame = 5
                self.shoot()
            if self.frame == len(self.animShoot):
                self.frame = 0
                self.shootPlayer = False

        if self.rect.right > 860:
            self.rect.right = 860
        if self.rect.left < 215:
            self.rect.left = 215
        if self.rect.top < 10:
            self.rect.top = 10
        if self.rect.bottom > 490:
            self.rect.bottom = 490

    def shoot(self):
        pea = Pea(self.rect.right+10, self.rect.top+27)
        game_setup.all_sprites.add(pea)
        game_setup.peas.add(pea)
