import pygame
import game_setup



class Doom(pygame.sprite.Sprite):

    def __init__(self, x,y, *group):
        super().__init__(*group)
        self.anim = [pygame.image.load('./img/DOOM_01.PNG'),
                     pygame.image.load('./img/DOOM_02.PNG'),
                     pygame.image.load('./img/DOOM_03.PNG'),
                     pygame.image.load('./img/DOOM_04.PNG'),
                     pygame.image.load('./img/DOOM_05.PNG'),
                     pygame.image.load('./img/DOOM_06.PNG'),
                     pygame.image.load('./img/DOOM_07.PNG'),
                     pygame.image.load('./img/DOOM_08.PNG'),
                     pygame.image.load('./img/DOOM_09.PNG'),
                     pygame.image.load('./img/DOOM_10.PNG'),
                     pygame.image.load('./img/DOOM_11.PNG'),
                     pygame.image.load('./img/DOOM_12.PNG'),
                     pygame.image.load('./img/DOOM_13.PNG'),
                     pygame.image.load('./img/DOOM_14.PNG'),
                     pygame.image.load('./img/DOOM_15.PNG'),
                     pygame.image.load('./img/DOOM_16.PNG'),
                     pygame.image.load('./img/DOOM_17.PNG'),
                     pygame.image.load('./img/DOOM_18.PNG'),
                     pygame.image.load('./img/DOOM_19.PNG'),
                     pygame.image.load('./img/DOOM_20.PNG'),
                     pygame.image.load('./img/DOOM_21.PNG'),
                     pygame.image.load('./img/DOOM_22.PNG'),
                     pygame.image.load('./img/DOOM_23.PNG'),
                     pygame.image.load('./img/DOOM_24.PNG'),
                     pygame.image.load('./img/DOOM_25.PNG'),
                     pygame.image.load('./img/DOOM_26.PNG'),
                     pygame.image.load('./img/DOOM_27.PNG'),
                     pygame.image.load('./img/DOOM_28.PNG'),
                     pygame.image.load('./img/DOOM_29.PNG'),]
        self.image = self.anim[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50
    def update(self):
 
        now = pygame.time.get_ticks()
        self.image = self.anim[self.frame]
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
        if self.frame == len(self.anim):
            self.kill()



