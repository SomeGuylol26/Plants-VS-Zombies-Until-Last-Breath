import pygame
import game_setup
from peashooter import Peashooter
from zombie import Zombie
from healthbar_peahooter import HB_P
from healthbar_base import HB_B


pygame.init()
WIDTH = 1000
HEIGHT = 514
FPS = 60
win = pygame.display.set_mode((WIDTH, HEIGHT))
img = pygame.image.load('./img/BackgroundDay.png')
clock = pygame.time.Clock()
pygame.display.set_caption('Plants VS Zombies: Until Last Breath')
pygame.mixer.music.load('./music/Music.mp3')
pygame.mixer.music.play(-1)
sound_brains = pygame.mixer.Sound("./music/groan6.ogg")


# Используем группы и объекты из game_setup

all_sprites = game_setup.all_sprites
hb_b = HB_B()
hb_p = HB_P()
all_sprites.add(hb_p)
all_sprites.add(hb_b)
kabooms = game_setup.kabooms
dooms = game_setup.dooms
peas = game_setup.peas
zombie = Zombie()
zombies = game_setup.zombies
peashooter_instance = Peashooter()
all_sprites.add(peashooter_instance)
all_sprites.add(zombie)
zombies.add(zombie)
score = 0
font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text,True, 'black')
    text_rect = text_surface.get_rect()
    text_rect.bottomleft = (x,y)
    surf.blit(text_surface,text_rect)
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    all_sprites.update()
    if zombie.rect.x == 150 and hb_b.hp > 0:
        hb_b.frame += 1
        hb_b.hp -= 1
        sound_brains.play()

    elif hb_b.hp == 0:
        pygame.mixer.music.stop()
        hb_b.hp -= 1
    if hb_b.time_end < 0:
        exit()

    nyam = pygame.sprite.spritecollide(peashooter_instance, zombies, False)
    if nyam and hb_p.hp > 0:
        sound_brains.play()
        hb_p.frame +=1
        hb_p.hp -= 1
        zombie.kill()
        zombie.death()
        zombie = Zombie()
        game_setup.all_sprites.add(zombie)
        game_setup.zombies.add(zombie)
    elif hb_p.hp < 1:
        peashooter_instance.death()
        peashooter_instance.kill()
        hb_p.hp = 1
        peashooter_instance.rect.y = 1000
        

        

        
        
    hits = pygame.sprite.groupcollide(zombies, peas, True, True)
    for hit in hits:
        score += 25
        zombie.death()
        zombie = Zombie()
        game_setup.all_sprites.add(zombie)
        game_setup.zombies.add(zombie)

    win.blit(img, (0,0))
    all_sprites.draw(win)
    draw_text(win, str(score), 50, 50, 510)
    pygame.display.update()