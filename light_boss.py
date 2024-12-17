import pygame

class LightBoss(pygame.sprite.Sprite):

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.anim = [pygame.image.load('./img/Boss/LightBoss_1.png').convert_alpha(),
                     pygame.image.load('./img/Boss/LightBoss_2.png').convert_alpha(),
                     pygame.image.load('./img/Boss/LightBoss_3.png').convert_alpha(),
                     pygame.image.load('./img/Boss/LightBoss_4.png').convert_alpha(),
                     pygame.image.load('./img/Boss/LightBoss_5.png').convert_alpha()]
        self.image = self.anim[0]
        self.rect = self.image.get_rect()
        self.frame = 0
        self.rect.x = x
        self.rect.y = y
        self.frame_rate = 360
        self.last_update = pygame.time.get_ticks()
        
    def update(self):
        now = pygame.time.get_ticks()
        self.image = self.anim[self.frame]
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
        if self.frame == len(self.anim):
            self.frame = 0
