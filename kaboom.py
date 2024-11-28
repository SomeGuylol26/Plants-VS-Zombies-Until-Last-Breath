import pygame



class Kaboom(pygame.sprite.Sprite):

    def __init__(self, x,y, *group):
        super().__init__(*group)
        self.anim = [pygame.image.load('./img/KABOOM_1.PNG'),
                     pygame.image.load('./img/KABOOM_2.PNG'),
                     pygame.image.load('./img/KABOOM_3.PNG'),
                     pygame.image.load('./img/KABOOM_4.PNG'),
                     pygame.image.load('./img/KABOOM_5.PNG'),
                     pygame.image.load('./img/KABOOM_6.PNG'),
                     pygame.image.load('./img/KABOOM_7.PNG')]
        self.image = self.anim[0]
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.right = x
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