from pygame import *

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Ping-Pong")
background = transform.scale(image.load('download.png'), (win_width, win_height))

font.init()
font1 = font.Font(None, 70)
lose1 = font1.render('Player 1 Lose!', True, (180, 0, 0))
lose2 = font1.render('Player 2 Lose!', True, (180, 0, 0))

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

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height:
            self.rect.y += self.speed

racket1 = Player1('racket.png', 20, win_height - 300, 30, 100, 5)
racket2 = Player2('racket.png', 650, win_height - 300, 30, 100, 5)
ball = GameSprite('tenis_ball.png', 200, 200, 50, 50, 50)

speed_x = 7
speed_y = 7

run = True
finish = False

clock = time.Clock()

while run:
    for e in event.get():
            if e.type == QUIT:
                run = False
    if not finish:
        window.blit(background, (0,0))

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
        if ball.rect.x > 700:
            finish = True
            window.blit(lose2, (200, 200))
        
        racket1.update()
        racket1.reset()
        racket2.update()
        racket2.reset()
        ball.reset()

        
        display.update()
        time.delay(50)
    clock.tick(60)