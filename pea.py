import pygame


class Pea(pygame.sprite.Sprite):

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.image.load('./img/Pea_1.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.right = x
        self.speedx = 10
    def update(self):
        self.rect.x += self.speedx
        if self.rect.right > 1100:
            self.kill()