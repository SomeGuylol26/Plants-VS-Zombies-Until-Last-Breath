import pygame
import game_setup
from peashooter import Peashooter
from zombie import Zombie
from healthbar_peahooter import HB_P
from healthbar_base import HB_B
from button_upgrade import Button
from repeater import Repeater
from galting_pea import GaltingPea
from conehead_zombie import ConeheadZombie
from buckethead_zombie import BucketheadZombie
from wavebar import WaveBar
from bar_head import BarHead
from text_center import TextCenter
from BOSS import BOSS
from light_boss import LightBoss
from healthbar_boss import HB_BOSS
from zombie_dancer import Zombie_Dancer
from light_attack import LightAttack

pygame.init()
black_screen = pygame.Surface((1000,514))
black_screen.fill('black')
black_screen.set_alpha(0)
WIDTH = 1000
HEIGHT = 514
FPS = 60
upgrade = 0
win = pygame.display.set_mode((WIDTH, HEIGHT))
img = pygame.image.load('./img/Bcg/BackgroundDay.png').convert()
clock = pygame.time.Clock()
pygame.display.set_caption('Plants VS Zombies: Until Last Breath')
pygame.display.set_icon(pygame.image.load('./img/icon.png'))
pygame.mixer.music.load('./music/Music.mp3')
pygame.mixer.music.play(-1)
sound_final = pygame.mixer.Sound('./music/finalfanfare.ogg')
sound_scream = pygame.mixer.Sound('./music/gargantudeath.ogg')
sound_sukhbir_2 = pygame.mixer.Sound('./music/sukhbir4.ogg')
sound_light = pygame.mixer.Sound('./music/lightsound.mp3')
sound_awooga = pygame.mixer.Sound('./music/awooga.ogg')
sound_brains = pygame.mixer.Sound("./music/groan6.ogg")
sound_groan_start = pygame.mixer.Sound('./music/groan2.ogg')
sound_splat = pygame.mixer.Sound('./music/splat.ogg')
sound_upgrade_1 = pygame.mixer.Sound('./music/chime.ogg')
sound_upgrade_2 = pygame.mixer.Sound('./music/achievement.ogg')
sound_groan_c = pygame.mixer.Sound('./music/groan.ogg')
sound_groan_b = pygame.mixer.Sound('./music/groan4.ogg')
sound_plastichit = pygame.mixer.Sound('./music/plastichit2.ogg')
sound_shieldhit = pygame.mixer.Sound('./music/shieldhit2.ogg')
sound_over = pygame.mixer.Sound("./music/losemusic.ogg")
sound_wave = pygame.mixer.Sound('./music/hugewave.ogg')
sound_finalwave = pygame.mixer.Sound('./music/finalwave.ogg')
sound_boss_laugh = pygame.mixer.Sound('./music/evillaugh.ogg')
all_sprites = game_setup.all_sprites
kabooms = game_setup.kabooms
sproings = game_setup.sproings
dooms = game_setup.dooms
peas = game_setup.peas
bosses = game_setup.bosses
hb = game_setup.hb
bh_zombies = game_setup.bh_zombies
ch_zombies = game_setup.ch_zombies
buttons = game_setup.buttons
zombie_dancers = game_setup.zombie_dancers
lights_attack = game_setup.lights_attack
zombie = Zombie()
zombies = game_setup.zombies
all_sprites.add(zombie)
zombies.add(zombie)
repeater = Repeater()
galting_pea = GaltingPea()
peashooter = Peashooter()
all_sprites.add(peashooter)
repeater.rect.y = 1000
galting_pea.rect.y = 1000
ch_zombie = ConeheadZombie()
bh_zombie = BucketheadZombie()
wb = WaveBar()
bar_h = BarHead(wb.rect.right, wb.rect.y)
tc = TextCenter()
all_sprites.add(tc)
hb.add(tc)
button_rect = pygame.Rect(10,120,100,88)
hb_b = HB_B()
hb_p = HB_P()
hb_boss = HB_BOSS()
button = Button()
hb.add([hb_p, hb_b])
all_sprites.add(button)
all_sprites.add(hb_b)
all_sprites.add(hb_p)
buttons.add(button)
zombie_dancer = Zombie_Dancer()
all_sprites.add(zombie_dancer)
zombie_dancers.add(zombie_dancer)
boss = BOSS()
hit_bull = False
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
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos) and button.upgrade == 1:
                button.transformation = 1
                sound_upgrade_1.play()
                button.frame += 1
                button.score -= 100
                button.kill_counter = 1
                peashooter.kill()
                all_sprites.add(repeater)
                repeater.rect.x = peashooter.rect.x-24
                repeater.rect.y = peashooter.rect.y-29
                peashooter.rect.y = 1000
                button.upgrade = 2
            if button_rect.collidepoint(event.pos) and button.upgrade == 3:
                button.transformation = 2
                sound_upgrade_2.play()
                button.kill()
                button.score -= 200
                repeater.kill()
                button.kill_counter = 2
                all_sprites.add(galting_pea)
                galting_pea.rect.x = repeater.rect.x
                galting_pea.rect.y = repeater.rect.y
                repeater.rect.y = 1000
                button.upgrade = 4
    all_sprites.update()
    if boss.rect.x == 600:
        all_sprites.add(hb_boss)
        hb.add(hb_boss)
        boss.rect.x = 601
        black_screen.set_alpha(255)
        wb.kill()
        lb = LightBoss(boss.rect.x, boss.rect.y-150)
        all_sprites.add(lb)
        hb.add(lb) 
        img = pygame.image.load('./img/Bcg/BackgroundNight.png').convert()
        boss.event_time = 150
        wb.wave = 4
    elif boss.rect.x == 600 and button.transformation == 1:
        repeater.rect.x = 300
    elif boss.rect.x == 600 and button.transformation == 2:
        galting_pea.rect.x = 300
    if wb.wave == 4 and repeater.rect.x > 400:
        repeater.rect.x = 400
    elif wb.wave == 4 and galting_pea.rect.x > 400:
        galting_pea.rect.x = 400
    if boss.attack == 1 and boss.time_attack < 0:
        boss.time_attack = 250
    if boss.time_attack == 200:
        light_attack = LightAttack()
        all_sprites.add(light_attack)
        lights_attack.add(light_attack)
        boss.time_attack -= 1
    elif boss.time_attack == 120:
        sound_light.play()
        light_attack.frame = 1
        boss.time_attack -= 1
    elif boss.time_attack == 60:
        hit_bull = False
        light_attack.rect.x = 2000        
        boss.time_attack -= 1
    if boss.event_time == 100:
        sound_boss_laugh.play()
        boss.event_time -= 1
    elif boss.event_time == 1:
        boss.attack = 1
        zombie_dancer.speedx = 2
        repeater.shoot_count = 0
        galting_pea.shoot_count = 0
        sound_light.play()
        black_screen.set_alpha(0)
        boss.event_time -= 1
        pygame.mixer.music.load('./music/BossMusic.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)
    if wb.time_progress == 0:
        wb.time_progress = 500
        wb.frame+= 1
        bar_h.rect.x -= 7
    if wb.frame == 7 and wb.wave == 0:
        bar_h.rect.x -= 7
        all_sprites.add(ch_zombie)
        ch_zombies.add(ch_zombie)
        wb.wave = 1
        tc.timer = 250
        tc.rect.x = 300
        tc.rect.y = 210
        sound_wave.play()
    if wb.frame == 16 and wb.wave == 1:
        bar_h.rect.x -= 7
        all_sprites.add(bh_zombie)
        bh_zombies.add(bh_zombie)
        wb.wave = 2
        tc.timer = 250
        tc.frame = 1
        tc.rect.x = 300
        tc.rect.y = 210
        sound_wave.play()
    if wb.frame == 24 and wb.wave == 2:
        sound_finalwave.play()
        wb.time_progress = -1
        zombie.spawn_zombie = 1
        zombie.kill()
        ch_zombie.spawn_zombie = 1
        ch_zombie.kill()
        bh_zombie.spawn_zombie = 1
        bh_zombie.kill()
        bar_h.rect.x -= 10
        wb.wave = 3
        tc.timer = 250
        tc.frame = 2
        tc.rect.x = 300
        tc.rect.y = 210
        pygame.mixer.music.stop()
    if tc.timer == 0 and wb.wave == 3:
        galting_pea.shoot_count = 999
        repeater.shoot_count = 999
        zombie_dancer = Zombie_Dancer()
        all_sprites.add(zombie_dancer)
        zombie_dancers.add(zombie_dancer)
        all_sprites.add(boss)
        bosses.add(boss)
        tc.timer -= 1
    if zombie.rect.x == 1400:
        sound_awooga.play()
        all_sprites.add(wb)
        hb.add(wb)
        all_sprites.add(bar_h)
        hb.add(bar_h)
    if zombie.rect.x == 1000:
        sound_groan_start.play()
    if ch_zombie.rect.x == 1000:
        sound_groan_c.play()
    if bh_zombie.rect.x == 1000:
        sound_groan_b.play()
    if zombie_dancer.rect.x == 999:
        sound_groan_start.play()
    if hb_boss.hp == 0:
        sound_light.stop()
        zombie_dancer.kill()
        lb.kill()
        light_attack.kill()
        boss.attack = 2
        pygame.mixer.music.stop()
        sound_scream.play()
        boss.position = 2
        boss.death_boss = 200
        hb_boss.hp -= 1
    elif boss.death_boss == 0:
        boss.death_boss -= 1
        boss.death()
        boss.kill()
        hb_boss.text_win = 200
    elif hb_boss.text_win == 1:
        sound_final.play()
        hb_boss.text_win = -1
        tc.timer = 400
        tc.rect.x = 280
        tc.rect.y = 210
        tc.frame = 3
        wb.wave = 5
    elif tc.timer < 0 and wb.wave > 4:
        exit()
    hits_z = pygame.sprite.groupcollide(zombies, peas, False, True)
    for hit in hits_z:
        zombie.hp -= 1
        sound_splat.play()
    if zombie.hp == 0:
        button.score += 5
        zombie.hp = 2
        zombie.spawn_zombie = 1
    if zombie.rect.x == 150 and hb_b.hp > 0:
        hb_b.frame += 1
        hb_b.hp -= 1
        sound_brains.play()
    hits_d = pygame.sprite.groupcollide(zombie_dancers, peas, False, True)
    for hit in hits_d:
        zombie_dancer.hp -= 1
        sound_splat.play()
    if zombie_dancer.hp == 0:
        button.score += 20
        zombie_dancer.hp = 4
        zombie_dancer.spawn_zombie = 1
    if zombie_dancer.rect.x == 150 and hb_b.hp > 0:
        hb_b.frame += 1
        hb_b.hp -= 1
        sound_brains.play()
    hits_c = pygame.sprite.groupcollide(ch_zombies, peas, False, True)
    for hit in hits_c:
        ch_zombie.hp -= 1
        sound_plastichit.play()
    if ch_zombie.hp == 0:
        button.score += 10
        ch_zombie.hp = 4
        ch_zombie.spawn_zombie = 1
    if ch_zombie.rect.x == 150 and hb_b.hp > 0:
        hb_b.frame += 1
        hb_b.hp -= 1
        sound_groan_c.play()
    hits_b = pygame.sprite.groupcollide(bh_zombies, peas, False, True)
    for hit in hits_b:
        bh_zombie.hp -= 1
        sound_shieldhit.play()
    if bh_zombie.hp == 0:
        button.score += 15
        bh_zombie.hp = 8
        bh_zombie.spawn_zombie = 1
    if bh_zombie.rect.x == 150 and hb_b.hp > 0:
        hb_b.frame += 1
        hb_b.hp -= 1
        sound_groan_b.play()
    elif hb_b.hp == 0:
        tc.timer = 2000
        tc.rect.x = 200
        tc.rect.y = 210
        tc.frame = 4
        pygame.mixer.music.stop()
        sound_over.play()
        hb_b.hp -= 1
    if hb_b.time_end < 0:
        exit()
    hits_boss = pygame.sprite.groupcollide(bosses, peas, False, True)
    for hit in hits_boss:
        sound_splat.play()
        hb_boss.hp -= 1
    nyam_pz = pygame.sprite.spritecollide(peashooter, zombies, False)
    if nyam_pz and hb_p.hp > 0:
        zombie.hp = 2
        sound_brains.play()
        zombie.spawn_zombie = 1
        hb_p.frame +=1
        hb_p.hp -= 1
    nyam_pc = pygame.sprite.spritecollide(peashooter, ch_zombies, False)
    if nyam_pc and hb_p.hp > 0:
        ch_zombie.hp = 4
        sound_groan_c.play()
        ch_zombie.spawn_zombie = 1
        hb_p.frame +=1
        hb_p.hp -= 1
    nyam_pb = pygame.sprite.spritecollide(peashooter, bh_zombies, False)
    if nyam_pb and hb_p.hp > 0:
        bh_zombie.hp = 8
        sound_groan_b.play()
        bh_zombie.spawn_zombie = 1
        hb_p.frame +=1
        hb_p.hp -= 1
    elif hb_p.hp < 1 and button.kill_counter == 0:
        button.kill()
        peashooter.death()
        peashooter.kill()
        hb_p.hp = 1
        peashooter.rect.y = 1000
    nyam_rz = pygame.sprite.spritecollide(repeater, zombies, False)
    if nyam_rz and hb_p.hp > 0:
        zombie.hp = 2
        sound_brains.play()
        zombie.spawn_zombie = 1
        hb_p.frame +=1
        hb_p.hp -= 1
    nyam_rc = pygame.sprite.spritecollide(repeater, ch_zombies, False)
    if nyam_rc and hb_p.hp > 0:
        ch_zombie.hp = 4
        sound_groan_c.play()
        ch_zombie.spawn_zombie = 1
        hb_p.frame +=1
        hb_p.hp -= 1
    nyam_rd = pygame.sprite.spritecollide(repeater, zombie_dancers, False)
    if nyam_rd and hb_p.hp > 0:
        zombie_dancer.hp = 4
        sound_sukhbir_2.play()
        zombie_dancer.spawn_zombie = 1
        hb_p.frame +=1
        hb_p.hp -= 1
    nyam_rb = pygame.sprite.spritecollide(repeater, bh_zombies, False)
    if nyam_rb and hb_p.hp > 0:
        bh_zombie.hp = 8
        sound_groan_b.play()
        bh_zombie.spawn_zombie = 1
        hb_p.frame +=1
        hb_p.hp -= 1
    elif hb_p.hp < 1 and button.kill_counter == 1:
        button.kill()
        repeater.death()
        repeater.kill()
        hb_p.hp = 1
        repeater.rect.y = 1000
    nyam_gz = pygame.sprite.spritecollide(galting_pea, zombies, False)
    if nyam_gz and hb_p.hp > 0:
        zombie.hp = 2
        sound_brains.play()
        zombie.spawn_zombie = 1
        hb_p.frame +=1
        hb_p.hp -= 1
    nyam_gc = pygame.sprite.spritecollide(galting_pea, ch_zombies, False)
    if nyam_gc and hb_p.hp > 0:
        ch_zombie.hp = 4
        sound_groan_c.play()
        ch_zombie.spawn_zombie = 1
        hb_p.frame +=1
        hb_p.hp -= 1
    nyam_gd = pygame.sprite.spritecollide(galting_pea, zombie_dancers, False)
    if nyam_gd and hb_p.hp > 0:
        zombie_dancer.hp = 4
        sound_sukhbir_2.play()
        zombie_dancer.spawn_zombie = 1
        hb_p.frame +=1
        hb_p.hp -= 1
    nyam_gb = pygame.sprite.spritecollide(galting_pea, bh_zombies, False)
    if nyam_gb and hb_p.hp > 0:
        bh_zombie.hp = 8
        sound_groan_b.play()
        bh_zombie.spawn_zombie = 1
        hb_p.frame +=1
        hb_p.hp -= 1
    elif hb_p.hp < 1 and button.kill_counter == 2:
        button.kill()
        galting_pea.death()
        galting_pea.kill()
        hb_p.hp = 1
        galting_pea.rect.y = 1000
    attack_hit_g = pygame.sprite.spritecollide(galting_pea, lights_attack, hit_bull)
    if attack_hit_g and light_attack.frame == 1 and hb_boss.hp > 0:
        hit_bull = True
        hb_p.frame += 1
        hb_p.hp -= 1
    attack_hit_r = pygame.sprite.spritecollide(repeater, lights_attack, hit_bull)
    if attack_hit_r and light_attack.frame == 1 and hb_boss.hp > 0:
        hit_bull = True
        hb_p.frame += 1
        hb_p.hp -= 1

    win.blit(img, (0,0))
    all_sprites.draw(win)
    hb.draw(win)
    buttons.draw(win)
    draw_text(win, str(button.score), 50, 50, 510)
    win.blit(black_screen,(0,0))
    pygame.display.update()