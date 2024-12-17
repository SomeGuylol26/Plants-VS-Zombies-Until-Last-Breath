import pygame

class TextCenter(pygame.sprite.Sprite):

    def __init__(self, *group):
        super().__init__(*group)
        self.anim = [pygame.image.load('./img/Text/WAVE_1.png').convert(),
                     pygame.image.load('./img/Text/WAVE_2.png').convert(),
                     pygame.image.load('./img/Text/WAVE_3.png').convert(),
                     pygame.image.load('./img/Text/YOUWIN.png').convert(),
                     pygame.image.load('./img/Text/GAMEOVER.png').convert()]
        self.image = self.anim[0]
        self.rect = self.image.get_rect()
        self.frame = 0
        self.rect.x = 2000
        self.rect.y = 2000
        self.timer = 0
        
    def update(self):
        self.image = self.anim[self.frame]
        self.timer -= 1
        if self.timer < 1:
            self.rect.x = 2000
            self.rect.y = 2000
