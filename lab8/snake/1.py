import pygame as pg
import random



pg.init()

W = H = 600

screen = pg.display.set_mode((W,H))
pg.display.set_caption("snake")
BLOCK_SIZE = 40

clock = pg.time.Clock()
FPS = 5

class Snake:
  def __init__(self):
      self.body = [[13, 10], [12, 10],[11,10]]
      self.dx = 1
      self.dy = 0
  
  def draw(self):
    for i, (x, y) in enumerate(self.body):


        color = (255,0,0) if i == 0 else (0,255,0)
        pg.draw.rect(screen, color, ((x * BLOCK_SIZE)%W, (y * BLOCK_SIZE)%H, BLOCK_SIZE, BLOCK_SIZE))
        
  
  def move(self):
    for i in range(len(self.body) - 1, 0, -1):
      self.body[i][0] = self.body[i - 1][0]
      self.body[i][1] = self.body[i - 1][1]

    self.body[0][0] += self.dx
    self.body[0][1] += self.dy

class Food:
    def __init__(self):
        self.position()
        self.image = pg.transform.scale(pg.image.load('1.png'),(BLOCK_SIZE,BLOCK_SIZE))
    def position(self):
        self.fx = ((random.randint(0,W))//BLOCK_SIZE)*BLOCK_SIZE
        self.fy = ((random.randint(0,H))//BLOCK_SIZE)*BLOCK_SIZE
    def draw(self):
        screen.blit(self.image,(self.fx,self.fy))

class Bigf:
    def __init__(self):
        self.pos()
        self.image = pg.transform.scale(pg.image.load('2.png'),(BLOCK_SIZE,BLOCK_SIZE))
    def pos(self):
        self.fx = ((random.randint(0,W))//BLOCK_SIZE)*BLOCK_SIZE
        self.fy = ((random.randint(0,H))//BLOCK_SIZE)*BLOCK_SIZE
    def draw(self):
        screen.blit(self.image,(self.fx,self.fy))



def draw_grid():
  image =  pg.transform.scale(pg.image.load('bg.png'),(W,H))
  screen.blit(image,(0,0))

snake = Snake()
fd = Food()
bg = Bigf()


Run = True
angle = 0
score = 0
timer = 15


while Run:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            Run = False
        if event.type == pg.KEYDOWN:
            if angle == 0:
                if event.key == pg.K_d:
                    snake.dx = 0
                    snake.dy = 1
                    angle = 270
                elif event.key == pg.K_a:
                    snake.dx = 0
                    snake.dy = -1 
                    angle = 90 
            elif angle == 90:
                if event.key == pg.K_d:
                    snake.dx = 1
                    snake.dy = 0
                    angle = 0
                elif event.key == pg.K_a:
                    snake.dx =-1
                    snake.dy = 0 
                    angle = 180
            elif angle == 180:
                if event.key == pg.K_d:
                    snake.dx = 0
                    snake.dy = -1
                    angle = 90
                elif event.key == pg.K_a:
                    snake.dx = 0
                    snake.dy = 1 
                    angle = 270
            elif angle == 270:
                if event.key == pg.K_d:
                    snake.dx = -1
                    snake.dy = 0
                    angle = 180
                elif event.key == pg.K_a:
                    snake.dx = 1
                    snake.dy = 0 
                    angle = 0             
    
    snake.move() 
    screen.fill((255,255,255))       
    draw_grid()       
    fd.draw()
    snake.draw()
    
    

    if (snake.body[0][0] * BLOCK_SIZE)%W == fd.fx and (snake.body[0][1] * BLOCK_SIZE)%H == fd.fy:
        snake.body.append([0, 0])
        fd.position()
        bg.pos()
        score +=1
        timer = 15

    for i in range(1,len(snake.body)):
        if snake.body[0][0] == snake.body[i][0] and snake.body[0][1] == snake.body[i][1]:
            Run = False
    if score%5==0 and score!=0:
        timer -=1
        if timer >= 0:
            bg.draw()
    
        
    
    if (snake.body[0][0] * BLOCK_SIZE)%W == bg.fx and (snake.body[0][1] * BLOCK_SIZE)%H == bg.fy:
        timer = 15 
        score +=1
        snake.body.append([0, 0])
        snake.body.append([0, 0])

    font = pg.font.Font(None, 30)
    text = font.render(f'Score: {score}', True, (255, 0, 0))
    screen.blit(text, (20, 20))
        
        
        
    pg.display.update()
    clock.tick(FPS)

        
    


            

