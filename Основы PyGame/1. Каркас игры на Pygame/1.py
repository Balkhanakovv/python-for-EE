import pygame

def main():    
    pygame.init()
    pygame.display.set_mode((600, 400))

    clock = pygame.time.Clock()
    FPS = 1
    while True:
        clock.tick(FPS)
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                return

        pygame.display.set_caption('Заголовок')
        pygame.display.update()

if __name__ == "__main__":
    main()
