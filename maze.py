#создай игру "Лабиринт"!
from turtle import window_height, window_width
from pygame import *

mixer.init()
mixer.music.load('dream.mp3')
mixer.music.play()

window_width = 700
window_height = 500
window = display.set_mode((window_width, window_height))
display.set_caption("Maze")
background = transform.scale(image.load('background.jpg'), (700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65, 65))
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
        if keys[K_d] and self.rect.x < window_width - 80:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < window_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 250:
            self.direction = 'right'
        if self.rect.x >= window_width - 85:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color = (color_1, color_2, color_3)
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

player = Player('body.png', 50, 400, 5)
enemy = Enemy('cyborg.png', 250, 40, 4)
finish = GameSprite('treasure.png', 580, 350, 10)
w1 = Wall(154, 205, 50, 120, 20, 450, 10)
w2 = Wall(154, 205, 50, 120, 480, 350, 10)
w3 = Wall(154, 205, 50, 120, 110, 10, 380)
w4 = Wall(154, 205, 50, 220, 20, 10, 380)
w5 = Wall(154, 205, 50, 470, 110, 10, 380)
w6 = Wall(154, 205, 50, 360, 200, 120, 10)
w7 = Wall(154, 205, 50, 360, 110, 10, 290)

font.init()
font1 = font.SysFont('Arial', 70)
win = font1.render('YOU WIN!', True, (255, 215, 0))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))
walls = [w1, w2, w3, w4, w5, w6, w7]
game = True
final = False
clock = time.Clock()
FPS  = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if not final == True:
        window.blit(background, (0, 0))
        player.update()
        player.reset()
        enemy.update()
        enemy.reset()
        finish.reset()
        for wall in walls:
            wall.draw_wall()
            if sprite.collide_rect(player, wall):
                final = True
                window.blit(lose, (200, 200))
        if sprite.collide_rect(player, finish):
            final = True
            window.blit(win, (200, 200))
        if sprite.collide_rect(player, enemy):
            final = True
            window.blit(lose, (200, 200))
    

    display.update()
    clock.tick(FPS)