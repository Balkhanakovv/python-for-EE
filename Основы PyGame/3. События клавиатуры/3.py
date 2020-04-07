import pygame

FPS = 60
W = 700
H = 300
WHITE = (255, 255, 255)
BLUE = (0, 70, 255)
RIGHT = "to the right"
LEFT = "to the left"
STOP = "stop"

pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

x = W // 2
y = H // 2
r = 50

motion = STOP

while 1:
    sc.fill(WHITE)

    pygame.draw.circle(sc, BLUE, (x, y), r)

    pygame.display.update()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 3
    elif keys[pygame.K_RIGHT]:
        x += 3
    elif keys[pygame.K_LEFT] < 1 and x < W // 2:
        while (x != W // 2):
            sc.fill(WHITE)
            pygame.draw.circle(sc, BLUE, (x, y), r)
            pygame.display.update()
            x += 3
            clock.tick(FPS)
    elif keys[pygame.K_RIGHT] < 1 and x > W // 2:
        while (x != W // 2):
            sc.fill(WHITE)
            pygame.draw.circle(sc, BLUE, (x, y), r)
            pygame.display.update()
            x -= 3
            clock.tick(FPS)


    clock.tick(FPS)