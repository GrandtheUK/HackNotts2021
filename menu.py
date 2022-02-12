import pygame, os
from config import *

class Menu:
    def __init__(self):
        self.screen = pygame.display.set_mode(DISPLAY)

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                