import pygame,sys,json

def drawLevel(screen,gridSize,tileSize):
    with open("levels/01-river.json") as f:
        level = json.load(f)
    print(level)

def drawGrid(screen,gridSize,tileSize):
    """Draws a grey and black grid to the screen"""
    background=pygame.Surface(screen.get_size())
    blackTile=pygame.Surface(tileSize)
    greyTile=pygame.Surface(tileSize)
    blackTile.fill((0,0,0))
    blackTile.fill((128,128,128))

    i=0
    j=0
    while i<gridSize[0]:
        while j<gridSize[1]:
            if (i%2==0) and (j%2==0):
                background.blit(blackTile,(i*tileSize[0],j*tileSize[1]))
            elif (i%2==0) and (j%2==1):
                background.blit(greyTile,(i*tileSize[0],j*tileSize[1]))
            elif (i%2==1) and (j%2==0):
                background.blit(greyTile,(i*tileSize[0],j*tileSize[1]))
            elif (i%2==1) and (j%2==1):
                background.blit(blackTile,(i*tileSize[0],j*tileSize[1]))
            j+=1
        i+=1
        j=0
    screen.blit(background,(0,0))

pygame.init()
screen = pygame.display.set_mode(DISPLAY)
pygame.display.set_caption("Fishing Game")

def main():
    DISPLAY=(1600,896)

def main():

    screenSize=screen.get_size()
    tileSize=[64,64]
    gridSize=[screenSize[0]/tileSize[0],screenSize[1]/tileSize[1]]

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250,250,250))
    drawGrid(screen,gridSize,tileSize)

    screen.blit(background, (0,0))
    drawGrid(screen,gridSize,tileSize)
    pygame.display.flip()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        pygame.display.flip()


if __name__ == "__main__":
    main()