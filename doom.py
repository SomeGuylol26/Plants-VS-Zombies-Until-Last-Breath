import pygame

class Doom(pygame.sprite.Sprite):
    def __init__(self, x,y, *group):
        super().__init__(*group)
        self.anim = [pygame.image.load('./img/Doom/DOOM_01.PNG').convert(),
                     pygame.image.load('./img/Doom/DOOM_02.PNG').convert(),
                     pygame.image.load('./img/Doom/DOOM_03.PNG').convert(),
                     pygame.image.load('./img/Doom/DOOM_04.PNG').convert(),
                     pygame.image.load('./img/Doom/DOOM_05.PNG').convert(),
                     pygame.image.load('./img/Doom/DOOM_06.PNG').convert(),
                     pygame.image.load('./img/Doom/DOOM_07.PNG').convert(),
                     pygame.image.load('./img/Doom/DOOM_08.PNG').convert(),
                     pygame.image.load('./img/Doom/DOOM_09.PNG').convert(),
                     pygame.image.load('./img/Doom/DOOM_10.PNG').convert(),
                     pygame.image.load('./img/Doom/DOOM_11.PNG').convert(),
                     pygame.image.load('./img/Doom/DOOM_12.PNG').convert(),
                     pygame.image.load('./img/Doom/DOOM_13.PNG').convert(),
                     pygame.image.load('./img/Doom/DOOM_14.PNG').convert(),
                     pygame.image.load('./img/Doom/DOOM_15.PNG').convert(),
                     pygame.image.load('./img/Doom/DOOM_16.PNG').convert(),
                     pygame.image.load('./img/Doom/DOOM_17.PNG').convert(),
                     pygame.image.load('./img/Doom/DOOM_18.PNG').convert(),
                     pygame.image.load('./img/Doom/DOOM_19.PNG').convert(),
                     pygame.image.load('./img/Doom/DOOM_20.PNG').convert(),
                     pygame.image.load('./img/Doom/DOOM_21.PNG').convert(),
                     pygame.image.load('./img/Doom/DOOM_22.PNG').convert(),
                     pygame.image.load('./img/Doom/DOOM_23.PNG').convert(),
                     pygame.image.load('./img/Doom/DOOM_24.PNG').convert(),
                     pygame.image.load('./img/Doom/DOOM_25.PNG').convert(),
                     pygame.image.load('./img/Doom/DOOM_26.PNG').convert(),
                     pygame.image.load('./img/Doom/DOOM_27.PNG').convert_alpha(),
                     pygame.image.load('./img/Doom/DOOM_28.PNG').convert_alpha(),
                     pygame.image.load('./img/Doom/DOOM_29.PNG').convert_alpha()]
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



