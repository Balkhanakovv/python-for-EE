import pygame

pygame.init()

W=200
H=100

circle1_x = 10
circle1_y = 10

circle2_x = 10
circle2_y = 50

sc = pygame.display.set_mode((300, 200))
clock = pygame.time.Clock()

surf = pygame.Surface((W, H))
surf.fill((255, 255, 255))
pygame.draw.circle(surf, (0, 0, 255), (circle1_x, circle1_y), 5) 
pygame.draw.circle(surf, (255, 0, 0), (circle2_x, circle2_y), 10)
sc.blit(surf, (50, 25))
pygame.display.update()

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    
    while circle1_x != W+20 and circle2_x != W+20:
        surf.fill((255, 255, 255))
        pygame.draw.circle(surf, (0, 0, 255), (circle1_x, circle1_y), 5) 
        pygame.draw.circle(surf, (255, 0, 0), (circle2_x, circle2_y), 10)
        circle1_x += 1
        circle2_x += 1
        sc.blit(surf, (50, 25))
        pygame.display.update()
        clock.tick(60)

    circle1_x = -10
    circle2_x = -10

    clock.tick(60)