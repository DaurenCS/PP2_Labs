import pygame

pygame.init()

H = 800
W = 800

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Sharik")

clock = pygame.time.Clock()
# Frame per second
FPS = 60

run = True

x = 100
y = 100

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= 3
    if pressed[pygame.K_DOWN]:
        y += 3
    if pressed[pygame.K_LEFT]:
        x -= 3
    if pressed[pygame.K_RIGHT]:
        x += 3
    
    screen.fill((255,255,255))
    pygame.draw.circle(screen,(255,0,0) , (x%800, y%800), 25)
    
    
    pygame.display.update()
    
    clock.tick(FPS)
