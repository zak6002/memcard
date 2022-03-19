from random import randint
from pygame import *

mixer.init()
mixer.music.load('Survive - Omniverse.mp3')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')

font.init()
font2 = font.SysFont('Arial', 36)
font1 = font.SysFont('Arial', 150)
win = font1.render('YOU WIN', 1, (0, 255, 0))
lose = font1.render('YOU LOSE', 1, (255, 0, 0))

img_back = "galaxy.jpg"
img_hero = "rocket.png"
img_bullet = 'bullet.png'
img_explore = 'explore.jpg'

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Shooter")
background = transform.scale(image.load(img_back), (win_width, win_height))
clock = time.Clock()

finish = False
run = True

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()

lost = 0
score = 0

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost += 1

rocet = Player(img_hero, 0, 350, 100, 130, 6)

bullets = sprite.Group()
monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy('ufo.png', randint(80, win_width - 80), 0, 100, 100, randint(1, 2))
    monsters.add(monster)

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                rocet.fire()
    
    if not finish:
        window.blit(background, (0,0))
        
        rocet.update()
        monsters.update()
        bullets.update()

        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score = score + 1
            monster = Enemy('ufo.png', randint(80, win_width - 80), 0, 100, 100, randint(1, 5))
            monsters.add(monster)

        

        rocet.reset()
        monsters.draw(window)
        bullets.draw(window)
        
        if score >= 15:
            window.blit(win, (70, 150))
            finish = True

        if lost >= 10 or sprite.spritecollide(rocet, monsters, False, False):
            window.blit(lose, (50, 150))
            finish = True

        text = font2.render('Счёт:' + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))

        text_lose = font2.render('Пропущено:' + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))

        display.update()
    
    clock.tick(60)