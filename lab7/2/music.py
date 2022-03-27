import pygame 
import datetime

pygame.init()

H = 500
W = 500

music = ['m1.mp3','m2.mp3','m3.mp3','m4.mp3']

clock = pygame.time.Clock()
FPS = 30

screen = pygame.display.set_mode((H,W))
pygame.display.set_caption("Music")

img = pygame.transform.scale(pygame.image.load('1.png'),(H,W))

run = True



def rot_center(image, angle, x, y):
    
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)
    screen.fill((255,255,255))
    screen.blit(rotated_image, new_rect)
angle = 0
x = 2
i = 0
while run:
    
    
    Time = datetime.datetime.now()
   
    sec = Time.second
    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and x == 2:
                pygame.mixer.music.load(music[i])
                pygame.mixer.music.play(-1)
                x = 1
                

            if event.key == pygame.K_SPACE and x == 0:
                pygame.mixer.music.unpause()
                x = 1
                
            elif event.key == pygame.K_SPACE and x == 1:
                pygame.mixer.music.pause()
                x = 0
            elif event.key == pygame.K_RIGHT:
                i+=1
                pygame.mixer.music.load(music[i%(len(music))])
                pygame.mixer.music.play(-1)
                x = 1
            elif event.key == pygame.K_LEFT:
                i-=1
                pygame.mixer.music.load(music[i%(len(music))])
                pygame.mixer.music.play(-1)
                x = 1
                
    if x == 1:
        rot_center(img,angle, H/2,W/2)
        angle+=1

   
    
    pygame.display.update()
    clock.tick(FPS)