import pygame
from pea import Pea
import game_setup
from doom import Doom

sound_throw = pygame.mixer.Sound("./music/throw.ogg")
sound_doom = pygame.mixer.Sound("./music/doomshroom.ogg")

class GaltingPea(pygame.sprite.Sprite):

    def __init__(self, *group):
        super().__init__(*group)
        self.anim = [pygame.image.load('./img/Glt/GaltingPeaIdle_1.png').convert(),
                     pygame.image.load('./img/Glt/GaltingPeaIdle_2.png').convert(),
                     pygame.image.load('./img/Glt/GaltingPeaIdle_3.png').convert(),
                     pygame.image.load('./img/Glt/GaltingPeaIdle_4.png').convert(),
                     pygame.image.load('./img/Glt/GaltingPeaIdle_5.png').convert(),
                     pygame.image.load('./img/Glt/GaltingPeaIdle_6.png').convert(),
                     pygame.image.load('./img/Glt/GaltingPeaIdle_7.png').convert(),
                     pygame.image.load('./img/Glt/GaltingPeaIdle_8.png').convert()]
        self.animShoot = [pygame.image.load('./img/Glt/GaltingPeaShoot_01.png').convert(),
                          pygame.image.load('./img/Glt/GaltingPeaShoot_02.png').convert(),
                          pygame.image.load('./img/Glt/GaltingPeaShoot_02.png').convert(),
                          pygame.image.load('./img/Glt/GaltingPeaShoot_03.png').convert(),
                          pygame.image.load('./img/Glt/GaltingPeaShoot_04.png').convert(),
                          pygame.image.load('./img/Glt/GaltingPeaShoot_04.png').convert(),
                          pygame.image.load('./img/Glt/GaltingPeaShoot_05.png').convert(),
                          pygame.image.load('./img/Glt/GaltingPeaShoot_06.png').convert(),
                          pygame.image.load('./img/Glt/GaltingPeaShoot_06.png').convert(),
                          pygame.image.load('./img/Glt/GaltingPeaShoot_07.png').convert(),
                          pygame.image.load('./img/Glt/GaltingPeaShoot_08.png').convert(),
                          pygame.image.load('./img/Glt/GaltingPeaShoot_08.png').convert(),
                          pygame.image.load('./img/Glt/GaltingPeaShoot_09.png').convert(),
                          pygame.image.load('./img/Glt/GaltingPeaShoot_10.png').convert(),
                          pygame.image.load('./img/Glt/GaltingPeaShoot_11.png').convert(),
                          pygame.image.load('./img/Glt/GaltingPeaShoot_12.png').convert()]
        self.image = self.anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = (1000/2, 514/2)
        self.speedx = 0
        self.speedy = 0
        self.frame = 0
        self.frame_shoot = 0
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
            self.shoot_count = 30
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
            self.frame_rate = 100
            self.image = self.animShoot[self.frame_shoot]
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.frame_shoot += 1
            if self.frame_shoot == 1:
                sound_throw.play()
                self.frame_shoot = 2
                self.shoot()
            if self.frame_shoot == 3:
                sound_throw.play()
                self.frame_shoot = 4
                self.shoot()
            if self.frame_shoot == 5:
                sound_throw.play()
                self.frame_shoot = 6
                self.shoot()
            if self.frame_shoot == 7:
                sound_throw.play()
                self.frame_shoot = 8
                self.shoot()
            if self.frame_shoot == len(self.animShoot):
                self.frame_shoot = 0
                self.shootPlayer = False
        if self.rect.right > 900:
            self.rect.right = 900
        if self.rect.left < 180:
            self.rect.left = 180
        if self.rect.top < -20:
            self.rect.top = -20
        if self.rect.bottom > 500:
            self.rect.bottom = 500
    def shoot(self):
        pea = Pea(self.rect.right+5, self.rect.top+55)
        game_setup.all_sprites.add(pea)
        game_setup.peas.add(pea)
    def death(self):
        sound_doom.play()
        doom = Doom(self.rect.centerx, self.rect.centery-90)
        game_setup.all_sprites.add(doom)
        game_setup.dooms.add(doom)

