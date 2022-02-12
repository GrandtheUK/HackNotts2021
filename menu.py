import pygame, os
from config import *
# import main

pygame.init()
pygame.font.init()
pygame.display.set_caption("Menu")
clock = pygame.time.Clock()

grey = (100, 100, 100)

def main():
    screen = pygame.display.set_mode(DISPLAY)
    screen.fill(grey)
    font = pygame.font.SysFont("Arial", 50)
    img = font.render('start', True, (255, 255, 255))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.blit(img, (20, 20))

        pygame.display.update()
        clock.tick(30)
    pygame.quit()

main()