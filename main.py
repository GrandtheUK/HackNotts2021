import pygame, sys, level, classes, menu, controlPanel
from tkinter import messagebox
from config import *

pygame.init()
screen = pygame.display.set_mode(WINDOW)
icon = pygame.image.load("./sprites/icon.png")
pygame.display.set_caption("Fishing Game")
pygame.display.set_icon(icon)

start_page = menu.Menu(screen)

def exit():
    answer = messagebox.askyesno('Exit', 'Are you sure you want to exit?')
    if answer == True:
        pygame.quit()
        sys.exit('Program terminated')

def main():
    tileGroup = pygame.sprite.Group()
    thisLevel = level.getLevelData("01-river")

    # fisherman sprite
    spriteGroup = pygame.sprite.Group()
    fisherman = classes.Fisherman(5*TILESIZE,7*TILESIZE,TILESIZE,TILESIZE*2,spriteGroup)
    spriteGroup.add(fisherman)
    
    floatPos = (200,200)
    # fishing line
    fishingLine = classes.Line(screen, (fisherman.rect.centerx - 5,fisherman.rect.top), floatPos)
    # create tile objects
    for i in range(GRID_WIDTH):
        for j in range(GRID_HEIGHT):
            id = thisLevel[j][i]
            tile = classes.Tile(id,i*TILESIZE,j*TILESIZE,TILESIZE,TILESIZE)
            tileGroup.add(tile)

    clock = pygame.time.Clock()

    controlPanelFunctions = {
        "exit" : exit
    }
    
    cp = controlPanel.ControlPanel(CTRL_PANEL_HEIGHT, DISPLAY[0], DISPLAY[1], controlPanelFunctions)

    start_page.run_menu()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                cp.check_cursor_pos(pygame.mouse.get_pos())
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if cp.mode == 0:
                        cp.mode = 1
                    elif cp.mode == 1:
                        cp.mode = 2
                        fisherman.cast(cp.angle, cp.power)
                    elif cp.mode == 2 and fisherman.float:
                        fisherman.reel()
                    if fisherman.state == "standing" and cp.mode == 2:
                        cp.angle = 0
                        cp.power = 0
                        cp.mode = 0
                
        keys = pygame.key.get_pressed()
        if fisherman.float:
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                fisherman.reel_in()

        tileGroup.draw(screen)
        showLine = False
        if fisherman.float:
            showLine = True
            fishingLine.endPos = fisherman.float.rect.center
        fishingLine.update(showLine)
        spriteGroup.update()
        spriteGroup.draw(screen)
        if fisherman.hookedFish:
            cp.fishBarVal = fisherman.hookedFish.energy
        cp.lineBarVal = fisherman.lineStrength
        cp.draw(screen)
        cp.update()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()