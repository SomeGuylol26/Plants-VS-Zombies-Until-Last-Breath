import pygame

class Kaboom(pygame.sprite.Sprite):

    def __init__(self, x,y, *group):
        super().__init__(*group)
        self.anim = [pygame.image.load('./img/Kbm/KABOOM_1.PNG').convert(),
                     pygame.image.load('./img/Kbm/KABOOM_2.PNG').convert(),
                     pygame.image.load('./img/Kbm/KABOOM_3.PNG').convert(),
                     pygame.image.load('./img/Kbm/KABOOM_4.PNG').convert(),
                     pygame.image.load('./img/Kbm/KABOOM_5.PNG').convert(),
                     pygame.image.load('./img/Kbm/KABOOM_6.PNG').convert(),
                     pygame.image.load('./img/Kbm/KABOOM_7.PNG').convert()]
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



