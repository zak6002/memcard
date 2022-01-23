#создай игру "Лабиринт"!
from pygame import *

mixer.init()
mixer.music.load('dream.mp3')
mixer.music.play()

window = display.set_mode((700, 500))
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

player = GameSprite('body.png', 50, 400, 10)
enemy = GameSprite('cyborg.png', 550, 220, 10)
finish = GameSprite('treasure.png', 580, 350, 10)
game = True
clock = time.Clock()
FPS  = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    window.blit(background, (0, 0))
    player.reset()
    enemy.reset()
    finish.reset()
    display.update()
    clock.tick(FPS)