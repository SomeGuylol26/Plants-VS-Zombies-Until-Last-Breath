import pygame
class Button(pygame.sprite.Sprite):

    def __init__(self, *group):
        super().__init__(*group)
        self.anim = [pygame.image.load('./img/Rpt/RepeaterButton_1.png').convert(),
                     pygame.image.load('./img/Rpt/RepeaterButton_2.png').convert(),
                     pygame.image.load('./img/Glt/GaltingPeaButton_1.png').convert(),
                     pygame.image.load('./img/Glt/GaltingPeaButton_2.png').convert()]
        self.image = self.anim[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (10,120)
        self.frame = 0
        self.score = 0
        self.upgrade = 0
        self.kill_counter = 0
        self.transformation = 0
        
    def update(self):
        self.image = self.anim[self.frame]
        if self.score > 99 and self.upgrade == 0:
            self.frame = 1
            self.upgrade = 1
        if self.score > 199 and self.upgrade == 2:
            self.frame = 3
            self.upgrade = 3


        