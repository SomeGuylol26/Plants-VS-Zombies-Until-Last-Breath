import pygame

class WaveBar(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.anim = [pygame.image.load('./img/Bar/wv_bar_01.PNG').convert(),
                     pygame.image.load('./img/Bar/wv_bar_02.PNG').convert(),
                     pygame.image.load('./img/Bar/wv_bar_03.PNG').convert(),
                     pygame.image.load('./img/Bar/wv_bar_04.PNG').convert(),
                     pygame.image.load('./img/Bar/wv_bar_05.PNG').convert(),
                     pygame.image.load('./img/Bar/wv_bar_06.PNG').convert(),
                     pygame.image.load('./img/Bar/wv_bar_07.PNG').convert(),
                     pygame.image.load('./img/Bar/wv_bar_08.PNG').convert(),
                     pygame.image.load('./img/Bar/wv_bar_09.PNG').convert(),
                     pygame.image.load('./img/Bar/wv_bar_10.PNG').convert(),
                     pygame.image.load('./img/Bar/wv_bar_11.PNG').convert(),
                     pygame.image.load('./img/Bar/wv_bar_12.PNG').convert(),
                     pygame.image.load('./img/Bar/wv_bar_13.PNG').convert(),
                     pygame.image.load('./img/Bar/wv_bar_14.PNG').convert(),
                     pygame.image.load('./img/Bar/wv_bar_15.PNG').convert(),
                     pygame.image.load('./img/Bar/wv_bar_16.PNG').convert(),
                     pygame.image.load('./img/Bar/wv_bar_17.PNG').convert(),
                     pygame.image.load('./img/Bar/wv_bar_18.PNG').convert(),
                     pygame.image.load('./img/Bar/wv_bar_19.PNG').convert(),
                     pygame.image.load('./img/Bar/wv_bar_20.PNG').convert(),
                     pygame.image.load('./img/Bar/wv_bar_21.PNG').convert(),
                     pygame.image.load('./img/Bar/wv_bar_22.PNG').convert(),
                     pygame.image.load('./img/Bar/wv_bar_23.PNG').convert(),
                     pygame.image.load('./img/Bar/wv_bar_24.PNG').convert(),
                     pygame.image.load('./img/Bar/wv_bar_25.PNG').convert()]

        self.image = self.anim[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (400, 10)
        self.frame = 0
        self.wave = 0
        self.time_progress = 750

    def update(self):
        self.time_progress -= 1
        self.image = self.anim[self.frame]




