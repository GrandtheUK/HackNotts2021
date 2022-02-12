import pygame

def main():#
    DISPLAY=(1600,900)
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Fishing Game")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250,250,250))

    screen.blit(background, (0,0))
    pygame.display.flip()

    while True:
        pygame.display.flip()

if __name__ == "__main__":
    main()