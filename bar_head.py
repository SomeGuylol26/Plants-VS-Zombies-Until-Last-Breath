import pygame

class BarHead(pygame.sprite.Sprite):

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.image.load('./img/Bar/wv_bar_27.png').convert()
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.right = x

        

