import pygame

class HB_B(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.anim = [pygame.image.load('./img/Bar/HB_B_1.PNG').convert(),
                     pygame.image.load('./img/Bar/HB_B_2.PNG').convert(),
                     pygame.image.load('./img/Bar/HB_B_3.PNG').convert(),
                     pygame.image.load('./img/Bar/HB_B_4.PNG').convert(),
                     pygame.image.load('./img/Bar/HB_B_4.PNG').convert(),
                     pygame.image.load('./img/Bar/HB_B_4.PNG').convert(),
                     ]
        self.image = self.anim[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (10, 10)
        self.frame = 0
        self.hp = 3
        self.time_end = 300

    def update(self):
        self.image = self.anim[self.frame]
        if self.hp == 0:
            self.hp == -1
        if self.hp == -1:
            self.time_end -= 1
