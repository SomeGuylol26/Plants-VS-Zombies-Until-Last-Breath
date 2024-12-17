import pygame

class Sproing(pygame.sprite.Sprite):

    def __init__(self, x,y, *group):
        super().__init__(*group)
        self.anim = [pygame.image.load('./img/Spg/SPROING_1.PNG').convert(),
                     pygame.image.load('./img/Spg/SPROING_2.PNG').convert(),
                     pygame.image.load('./img/Spg/SPROING_3.PNG').convert(),
                     pygame.image.load('./img/Spg/SPROING_4.PNG').convert(),
                     pygame.image.load('./img/Spg/SPROING_5.PNG').convert(),
                     pygame.image.load('./img/Spg/SPROING_6.PNG').convert(),
                     pygame.image.load('./img/Spg/SPROING_7.PNG').convert(),
                     pygame.image.load('./img/Spg/SPROING_8.PNG').convert(),
                     pygame.image.load('./img/Spg/SPROING_9.PNG').convert()]
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



