import pygame

WHITE = (255, 255, 255)
RED = (225, 0, 50)
BLUE = (0, 0, 225) 

W = 400
H = 300
FPS = 60

x = 0
y = 0

pygame.init()
sc = pygame.display.set_mode((W, H))
sc.fill(WHITE)
pygame.display.update()

clock = pygame.time.Clock()

while 1:  
    x = 0
    y = H    
    circle_pos = (x, y)
    pygame.draw.circle(sc, BLUE, circle_pos, 20)    
    pygame.display.update()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

        pressed = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        if pressed[0]:    
            y = H
            x = pos[0]         
            circle_pos = (x, y)
            pygame.draw.circle(sc, BLUE, circle_pos, 20)    
            pygame.display.update()
            while circle_pos != pos:
                sc.fill(WHITE)
                y -= 1
                circle_pos = (x, y)
                pygame.draw.circle(sc, BLUE, circle_pos, 20)    
                pygame.display.update()
                clock.tick(FPS)
            
            sc.fill(WHITE)
            pygame.draw.rect(sc, RED, (pos[0]-10, pos[1]-10, 20, 20))
            pygame.display.update()

    clock.tick(FPS)