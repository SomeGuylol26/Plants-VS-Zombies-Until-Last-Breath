import pygame

pygame.init()
WIDTH = 1000
HEIGHT = 514
FPS = 60
win = pygame.display.set_mode((WIDTH, HEIGHT))
img = pygame.image.load('BackgroundDay.png')
clock = pygame.time.Clock()
pygame.display.set_caption('Plants VS Zombies: Until Last Breath')
pygame.mixer.music.load('Music.mp3')
pygame.mixer.music.play(-1)

class Peashooter(pygame.sprite.Sprite):

    def __init__(self, *group):
        super().__init__(*group)
        self.anim = [pygame.image.load('PeashooterIdle_1.png'),
                     pygame.image.load('PeashooterIdle_2.png'),
                     pygame.image.load('PeashooterIdle_3.png'),
                     pygame.image.load('PeashooterIdle_4.png'),
                     pygame.image.load('PeashooterIdle_5.png'),
                     pygame.image.load('PeashooterIdle_6.png'),
                     pygame.image.load('PeashooterIdle_7.png'),
                     pygame.image.load('PeashooterIdle_8.png') ]
        self.image = self.anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.speedx = 0
        self.speedy = 0
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 150
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
             self.last_update = now
             self.frame += 1
             if self.frame == len(self.anim):
                  self.frame = 0
        self.image = self.anim[self.frame]
        self.speedx = 0
        self.speedy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speedx -= 7
        if keys[pygame.K_RIGHT]:
            self.speedx += 7
        self.rect.x += self.speedx
        if keys[pygame.K_UP]:
            self.speedy -= 7
        if keys[pygame.K_DOWN]:
            self.speedy += 7
        self.rect.y += self.speedy

        if self.rect.right > 860:
            self.rect.right = 860
        if self.rect.left < 215:
             self.rect.left = 215
        if self.rect.top < 10:
             self.rect.top = 10
        if self.rect.bottom > 490:
             self.rect.bottom = 490
             
all_sprites = pygame.sprite.Group()
peashooter = Peashooter()
all_sprites.add(peashooter)

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    all_sprites.update()
    win.blit(img, (0,0))
    all_sprites.draw(win)

    pygame.display.update()



            