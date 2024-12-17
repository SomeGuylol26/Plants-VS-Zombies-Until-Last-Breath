import pygame
import random
from BOSS import BOSS


class LightAttack(pygame.sprite.Sprite):

    def __init__(self, *group):
        super().__init__(*group)
        self.anim = [pygame.image.load('./img/Boss/LightAttack_1.png').convert(),
                     pygame.image.load('./img/Boss/LightAttack_2.png').convert_alpha()]
        self.image = self.anim[0]
        self.rect = self.image.get_rect()
        self.frame = 0
        self.rect.x = 250
        self.rect.y = 2000
        self.position = random.randrange(1,3)
    def update(self):
        self.image = self.anim[self.frame]
        if self.rect.x == 2000:
            self.kill()
        if self.position == 1:
            self.rect.y = 80
        elif self.position == 2:
            self.rect.y = 300

