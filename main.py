
import pygame, sys, level, classes
from config import *


def main():

    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Fishing Game")

    tileGroup = pygame.sprite.Group()
    thisLevel = level.getLevelData("01-river")

    # fisherman sprite
    spriteGroup = pygame.sprite.Group()
    fisherman = classes.Fisherman(5*TILESIZE,7*TILESIZE,TILESIZE,TILESIZE)
    spriteGroup.add(fisherman)

    # fishing line
    fishingLine = classes.Line(screen, fisherman.rect.midtop, (200,200))

    for i in range(GRID_WIDTH):
        for j in range(GRID_HEIGHT):
            id = thisLevel[j][i]
            tile = classes.Tile(id,i*TILESIZE,j*TILESIZE,TILESIZE,TILESIZE)
            tileGroup.add(tile)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        tileGroup.draw(screen)
        fishingLine.update()
        spriteGroup.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()