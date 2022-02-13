from random import randint
from pygame import *

mixer.init()
mixer.music.load('Survive - Omniverse.mp3')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')

img_back = "galaxy.jpg"
img_hero = "rocket.png"

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
    def fire():
        pass
lost = 0

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost += 1

enemy = Enemy('ufo.png', randint(10, 600), 0, 100, 100, randint(2, 5))
rocet = Player(img_hero, 0, 350, 100, 130, 5)

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    if not finish:
        window.blit(background, (0,0))
        rocet.reset()
        rocet.update()
        enemy.reset()
        enemy.update()
        display.update()
    clock.tick(60)