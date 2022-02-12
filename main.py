
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
    fisherman = classes.Fisherman(5*TILESIZE,7*TILESIZE,TILESIZE,TILESIZE*2,spriteGroup)
    spriteGroup.add(fisherman)

    floatPos = (200,200)
    # fishing line
    fishingLine = classes.Line(screen, fisherman.rect.midtop, floatPos)

    for i in range(GRID_WIDTH):
        for j in range(GRID_HEIGHT):
            id = thisLevel[j][i]
            tile = classes.Tile(id,i*TILESIZE,j*TILESIZE,TILESIZE,TILESIZE)
            tileGroup.add(tile)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if fisherman.float:
                    if event.key == pygame.K_UP:
                        fisherman.float.move(0,-10)
                    if event.key == pygame.K_DOWN:
                        fisherman.float.move(0,10)
                    if event.key == pygame.K_RIGHT:
                        fisherman.float.move(10,0)
                    if event.key == pygame.K_LEFT:
                        fisherman.float.move(-10,0)
                if event.key == pygame.K_SPACE:
                    fisherman.cast()

        tileGroup.draw(screen)
        showLine = False
        if fisherman.float:
            showLine = True
            fishingLine.endPos = fisherman.float.rect.center
        fishingLine.update(showLine)
        spriteGroup.update()
        spriteGroup.draw(screen)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()