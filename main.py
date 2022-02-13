import pygame, sys, level, classes, menu, controlPanel
from config import *

pygame.init()
screen = pygame.display.set_mode(WINDOW)
icon = pygame.image.load("./sprites/icon.png")
pygame.display.set_caption("Fishing Game")
pygame.display.set_icon(icon)

start_page = menu.Menu(screen)

def main():
    menuRunning = True

    tileGroup = pygame.sprite.Group()
    thisLevel = level.getLevelData("01-river")

    # fisherman sprite
    spriteGroup = pygame.sprite.Group()
    fisherman = classes.Fisherman(5*TILESIZE,7*TILESIZE,TILESIZE,TILESIZE*2,spriteGroup)
    spriteGroup.add(fisherman)

    floatPos = (200,200)
    # fishing line
    fishingLine = classes.Line(screen, (fisherman.rect.centerx + 10,fisherman.rect.top + 10), floatPos)

    for i in range(GRID_WIDTH):
        for j in range(GRID_HEIGHT):
            id = thisLevel[j][i]
            tile = classes.Tile(id,i*TILESIZE,j*TILESIZE,TILESIZE,TILESIZE)
            tileGroup.add(tile)

    clock = pygame.time.Clock()

    controlPanelFunctions = {
        "reel_in" : fisherman.reel_in
    }

    cp = controlPanel.ControlPanel(CTRL_PANEL_HEIGHT, DISPLAY[0], DISPLAY[1], controlPanelFunctions)

    while True:
        while menuRunning:
            start_page.run_menu()
            menuRunning = start_page.getState()

        while menuRunning == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    cp.check_cursor_pos(pygame.mouse.get_pos())
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if fisherman.float:
                            fisherman.reel()
                        else:
                            fisherman.cast()
                    
            keys = pygame.key.get_pressed()
            if fisherman.float:
                if keys[pygame.K_UP] or keys[pygame.K_w]:
                    floatPos = (floatPos[0], floatPos[1] - BOBBER_TRAVEL_SPEED)
                    fisherman.float.target = floatPos
                elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    floatPos = (floatPos[0], floatPos[1] + BOBBER_TRAVEL_SPEED)
                    fisherman.float.target = floatPos
                elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    floatPos = (floatPos[0] - BOBBER_TRAVEL_SPEED, floatPos[1])
                    fisherman.float.target = floatPos
                elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    floatPos = (floatPos[0] + BOBBER_TRAVEL_SPEED, floatPos[1])
                    fisherman.float.target = floatPos

            tileGroup.draw(screen)
            showLine = False
            if fisherman.float:
                showLine = True
                fishingLine.endPos = fisherman.float.rect.center
            fishingLine.update(showLine)
            spriteGroup.update()
            spriteGroup.draw(screen)
            cp.draw(screen)
            cp.update()

            pygame.display.flip()
            clock.tick(60)

if __name__ == "__main__":
    main()