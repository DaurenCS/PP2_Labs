import pygame 
import datetime

pygame.init()
heigh = 800
weigh = 800
screen = pygame.display.set_mode((heigh,weigh))
pygame.display.set_caption("Clock")

image3 = pygame.transform.scale(pygame.image.load('img3.jpg'),(heigh,weigh))
image1 = pygame.transform.scale(pygame.image.load('img1.png'),(heigh,weigh))
image2 = pygame.transform.scale(pygame.image.load('img2.png'),(heigh,weigh))

clock = pygame.time.Clock()
FPS = 60

run = True 


def rot_center(image, angle, x, y):
    
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)
    screen.blit(rotated_image, new_rect)

    

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    Time = datetime.datetime.now()
    min = Time.minute
    hour = Time.hour
    sec = Time.second


    screen.fill((255,255,255))
    screen.blit(image3, (0, 0))

    
    # min
    
    alpha = min*(360/60)
    rot_center(image2, -alpha, heigh/2, weigh/2  )
    
     # hour
    
    alpha = hour*(400/12)
    rot_center(image1, -alpha, heigh/2, weigh/2  )

   
    pygame.display.flip()
    clock.tick(FPS)
 

    




