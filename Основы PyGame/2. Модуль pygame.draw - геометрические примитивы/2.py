import pygame

FPS = 60
WIN_WIDTH = 500
WIN_HEIGHT = 100

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

pygame.init()

clock = pygame.time.Clock()

sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

r =30
x= 0 - r
y = WIN_HEIGHT // 2

while 1:
    sc.fill(WHITE)

    for i in pygame.event.get():
        if i.type == pygame.QUIT: exit()

    pygame.draw.circle(sc, BLUE, (x, y), r)
    pygame.display.update()

    if x >= WIN_WIDTH + r:
        x = 0 - r
    else:
        x += 2

    clock.tick(FPS)
