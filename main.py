
import pygame, sys, level, classes
from config import *

pygame.init()
screen = pygame.display.set_mode(DISPLAY)
pygame.display.set_caption("Fishing Game")

def main():

    tileGroup = pygame.sprite.Group()
    thisLevel = level.getLevelData("01-river")

    # fisherman sprite
    spriteGroup = pygame.sprite.Group()
    fisherman = classes.Fisherman(5*TILESIZE,7*TILESIZE,TILESIZE,TILESIZE*2)
    spriteGroup.add(fisherman)

    floatPos = (200,200)
    # fishing line
    fishingLine = classes.Line(screen, fisherman.rect.midtop, floatPos)

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

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
                floatPos = (floatPos[0], floatPos[1] - BOBBER_TRAVEL_SPEED)
                fishingLine.set_endPos(floatPos)
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                floatPos = (floatPos[0], floatPos[1] + BOBBER_TRAVEL_SPEED)
                fishingLine.set_endPos(floatPos)
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                floatPos = (floatPos[0] - BOBBER_TRAVEL_SPEED, floatPos[1])
                fishingLine.set_endPos(floatPos)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                floatPos = (floatPos[0] + BOBBER_TRAVEL_SPEED, floatPos[1])
                fishingLine.set_endPos(floatPos)

        tileGroup.draw(screen)
        fishingLine.update()
        spriteGroup.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()