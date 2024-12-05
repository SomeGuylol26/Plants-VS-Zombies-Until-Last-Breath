import pygame

class HB_P(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.anim = [pygame.image.load('./img/HB_P_1.PNG'),
                     pygame.image.load('./img/HB_P_2.PNG'),
                     pygame.image.load('./img/HB_P_3.PNG'),
                     pygame.image.load('./img/HB_P_4.PNG'),
                     pygame.image.load('./img/HB_P_5.PNG'),
                     pygame.image.load('./img/HB_P_6.PNG')]
        self.image = self.anim[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (10, 70)
        self.frame = 0
        self.hp = 5

    def update(self):
        self.image = self.anim[self.frame]
