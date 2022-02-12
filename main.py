import pygame, sys, level

TILESIZE = 64

def drawTestGrid(screen,gridSize,TILESIZE):
    """Draws a grey and black grid to the screen"""
    background=pygame.Surface(screen.get_size())
    blackTile=pygame.Surface((TILESIZE, TILESIZE))
    greyTile=pygame.Surface((TILESIZE, TILESIZE))
    blackTile.fill((0,0,0))
    blackTile.fill((128,128,128))

    i=0
    j=0
    while i<gridSize[0]:
        while j<gridSize[1]:
            if (i%2==0) and (j%2==0):
                background.blit(blackTile,(i*TILESIZE,j*TILESIZE))
            elif (i%2==0) and (j%2==1):
                background.blit(greyTile,(i*TILESIZE,j*TILESIZE))
            elif (i%2==1) and (j%2==0):
                background.blit(greyTile,(i*TILESIZE,j*TILESIZE))
            elif (i%2==1) and (j%2==1):
                background.blit(blackTile,(i*TILESIZE,j*TILESIZE))
            j+=1
        i+=1
        j=0
    screen.blit(background,(0,0))


def main():
    DISPLAY=(TILESIZE*12, TILESIZE*9)

    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Fishing Game")

    screenSize=screen.get_size()
    gridSize=[screenSize[0]/TILESIZE,screenSize[1]/TILESIZE]

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250,250,250))
    drawTestGrid(screen,gridSize,TILESIZE)

    screen.blit(background, (0,0))
    drawTestGrid(screen,gridSize,TILESIZE)
    pygame.display.flip()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        pygame.display.flip()

if __name__ == "__main__":
    main()