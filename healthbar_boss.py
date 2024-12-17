import pygame

class HB_BOSS(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.anim = [pygame.image.load('./img/Bar/hb_boss_01.PNG').convert(),
                     pygame.image.load('./img/Bar/hb_boss_06.PNG').convert(),
                     pygame.image.load('./img/Bar/hb_boss_11.PNG').convert(),
                     pygame.image.load('./img/Bar/hb_boss_20.PNG').convert(),
                     pygame.image.load('./img/Bar/hb_boss_26.PNG').convert()]
        self.image = self.anim[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (400, 2)
        self.frame = 0
        self.hp = 200
        self.text_win = 0

    def update(self):
        self.text_win-= 1
        self.image = self.anim[self.frame]
        if self.hp == 152:
            self.frame = 1
        elif self.hp == 100:
            self.frame = 2
        elif self.hp == 52:
            self.frame = 3
        elif self.hp == 0:
            self.frame = 4



