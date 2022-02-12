import pygame, os
from pygame import MOUSEBUTTONDOWN
from config import *

class Menu:
    def __init__(self, screen):
        self.grey = (100, 100, 100)

        self.screen = screen
        self.screen.fill(self.grey)

        self.alignCenter = DISPLAY[0]/2, DISPLAY[1]/2

        self.start_button = pygame.image.load("start.png").convert()
        self.start_rect = self.start_button.get_rect()
        self.start_rect.center = self.alignCenter
        self.run = True

    def run_menu(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.start_button.get_rect(center = (self.alignCenter)).collidepoint(pos):
                        self.run = False
                
            self.screen.blit(self.start_button, self.start_rect)

            pygame.display.update()
    
    def getState(self):
        return self.run