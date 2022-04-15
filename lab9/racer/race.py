from tkinter import CENTER
import pygame as pg
import random
import time


    
pg.init()
speed = 10
H = 400
W = 600

screen = pg.display.set_mode((H,W))
pg.display.set_caption("Racer")
        

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('pl.png')
        self.rect = self.image.get_rect(center = (W//2,H+100))
        
    def move(self):
        prs = pg.key.get_pressed()
        if prs[pg.K_d]:
            self.rect.move_ip(speed, 0)
        if prs[pg.K_a]:
            self.rect.move_ip(speed*(-1), 0)
    def update(self):
        screen.blit(self.image,self.rect)
        self.move()

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('Enemy.png')
        self.rect = self.image.get_rect(center = (random.choice([80,190,320]),random.choice([-180,-50])))
        
    def move(self):
        
        if self.rect.top > H+500:
            self.top = 0
            self.rect.center = (random.choice([80,190,320]),random.choice([-180,-50]))
        else:
            self.rect.move_ip(0, speed)
    def update(self):
        screen.blit(self.image,self.rect)
        self.move()

class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image =  pg.transform.scale(pg.image.load('coin.png'),(50,50))
        self.rect = self.image.get_rect(center =(random.choice([80,190,320]),random.randint(-500,-90)))
    def move(self):
        
        if self.rect.top > H+500:
            self.top = -500
            self.rect.center = (random.choice([80,190,320]),random.randint(-500,-90))
        else:
            self.rect.move_ip(0, speed)
    def update(self):
        screen.blit(self.image,self.rect)
        self.move()   

        

clock = pg.time.Clock()
FPS = 60


img = pg.transform.scale(pg.image.load('1.png'),(H,W))


#Background

def bckg(y):
    rel_y = y% img.get_rect().height
    screen.blit(img, (0, (rel_y-img.get_rect().height)))
    if  rel_y < W:
        screen.blit(img, (0,rel_y))

          

    

    
    
pg.mixer.music.load('1.wav')
pg.mixer.music.play(-1)    
not_paused = True
run = True
score = 0
y = 0
# Class

player = Player()
cars = Enemy()

coins = Coin()

enemies = pg.sprite.Group()
coins_group = pg.sprite.Group()
all_gr = pg.sprite.Group()

enemies.add(cars)

coins_group.add(coins)
all_gr.add(cars)
all_gr.add(player)
all_gr.add(coins)








while run:

    for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    not_paused = True


    
    if not_paused:
    

        bckg(y)
        y += 5
        

        if pg.sprite.spritecollideany(player, enemies):
            pg.mixer.music.load('crash.wav')
            pg.mixer.music.play(0) 
            not_paused = False
        
            
            

        if pg.sprite.spritecollideany(player,coins_group):
            
            for item in coins_group:
                item.kill()
            coins1 = Coin()
            coins_group.add(coins1)
            if score == 3 :
                cars = Enemy()
            all_gr.add(cars)
            all_gr.add(coins1)
            screen.blit(img, (0,0))
            score+=1
                
        all_gr.update()

        font = pg.font.Font(None, 30)
        text = font.render(f'Score: {score}', True, (255, 0, 0))
        screen.blit(text, (20, 20))

        
             


        pg.display.update()
        clock.tick(FPS)
    elif not_paused == False:
        screen.fill((255,0,0))
        
        font = pg.font.Font(None, 60)
        text1 = font.render('Game Over!!' ,True, (255, 255, 255))
        text = font.render( f'your score is {score}', True, (255, 255, 255))
        screen.blit(text1, (50, 200))
        screen.blit(text, (50, 250))
        
        

        pg.display.update()
        clock.tick(FPS)

        


