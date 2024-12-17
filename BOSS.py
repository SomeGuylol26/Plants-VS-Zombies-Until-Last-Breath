import pygame
from sproing import Sproing
import game_setup

sound_explosion = pygame.mixer.Sound("./music/explosion.ogg")
sound_thump = pygame.mixer.Sound('./music/gargantuar_thump.ogg')

class BOSS(pygame.sprite.Sprite):

    def __init__(self, *group):
        super().__init__(*group)
        self.anim = [pygame.image.load('./img/Boss/BOSSWALKING_1.png'),
                     pygame.image.load('./img/Boss/BOSSWALKING_1.png'),
                     pygame.image.load('./img/Boss/BOSSWALKING_2.png'),
                     pygame.image.load('./img/Boss/BOSSWALKING_3.png'),
                     pygame.image.load('./img/Boss/BOSSWALKING_3.png'),
                     pygame.image.load('./img/Boss/BOSSWALKING_4.png'),
                     pygame.image.load('./img/Boss/BOSSWALKING_1.png'),
                     pygame.image.load('./img/Boss/BOSSWALKING_1.png'),
                     pygame.image.load('./img/Boss/BOSSWALKING_2.png'),
                     pygame.image.load('./img/Boss/BOSSWALKING_3.png'),
                     pygame.image.load('./img/Boss/BOSSWALKING_3.png'),
                     pygame.image.load('./img/Boss/BOSSWALKING_4.png')] 
        self.anim_idle = [pygame.image.load('./img/Boss/BOSSIDLE_01.png').convert(),
                          pygame.image.load('./img/Boss/BOSSIDLE_02.png').convert(),
                          pygame.image.load('./img/Boss/BOSSIDLE_03.png').convert(),
                          pygame.image.load('./img/Boss/BOSSIDLE_04.png').convert(),
                          pygame.image.load('./img/Boss/BOSSIDLE_05.png').convert(),
                          pygame.image.load('./img/Boss/BOSSIDLE_06.png').convert(),
                          pygame.image.load('./img/Boss/BOSSIDLE_07.png').convert(),
                          pygame.image.load('./img/Boss/BOSSIDLE_08.png').convert(),
                          pygame.image.load('./img/Boss/BOSSIDLE_09.png').convert(),
                          pygame.image.load('./img/Boss/BOSSIDLE_10.png').convert(),
                          pygame.image.load('./img/Boss/BOSSIDLE_11.png').convert(),
                          pygame.image.load('./img/Boss/BOSSIDLE_12.png').convert()]
        self.image = self.anim[0]
        self.rect = self.image.get_rect()
        self.speedx = 2
        self.rect.x = 1600
        self.rect.y = 50
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 180
        self.hp = 2
        self.position = 0
        self.event_time = 0
        self.time_attack = 0
        self.attack = 0
        self.death_boss = -1
        
    def update(self):
        self.death_boss -= 1
        self.time_attack -= 1
        self.event_time -= 1
        self.rect.x -= self.speedx
        now = pygame.time.get_ticks()
        if self.position == 0:
            self.frame_rate = 360
            self.image = self.anim[self.frame]
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.frame += 1
            if self.frame == 0 or self.frame == 3 or self.frame == 6 or self.frame == 9:
                sound_thump.play()
                self.frame += 1
            if self.frame == len(self.anim):
                self.frame = 0
        elif self.position == 1:
            self.frame_rate = 180
            self.speedx = 0
            self.image = self.anim_idle[self.frame]
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.frame += 1
            if self.frame == len(self.anim):
                self.frame = 0
        elif self.position == 2:
            self.frame_rate = 50
            self.image = self.anim_idle[self.frame]
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.frame += 1
            if self.frame == len(self.anim):
                self.frame = 0
        if self.rect.x == 600:
            self.position = 1

    def death(self):
        sound_explosion.play()
        sproing = Sproing(self.rect.centerx, self.rect.centery)
        game_setup.all_sprites.add(sproing)
        game_setup.kabooms.add(sproing)
