import pygame, sys, level, classes

TILESIZE = 64


def main():
    DISPLAY=(TILESIZE*12, TILESIZE*9)

    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Fishing Game")

    tileGroup = pygame.sprite.Group()
    thisLevel = level.getLevelData("01-river")

    for i in range(12):
        for j in range(9):
            id = thisLevel[j][i]
            tile = classes.Tile(id,i*TILESIZE,j*TILESIZE,TILESIZE,TILESIZE)
            tileGroup.add(tile)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        tileGroup.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()