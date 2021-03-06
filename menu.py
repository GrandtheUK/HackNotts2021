import pygame, os, sys
from pygame import MOUSEBUTTONDOWN
from config import *

class Menu:
    def __init__(self, screen):
        self.white = (255, 255, 255)

        self.screen = screen
        self.screen.fill(self.white)

        self.start_button_image = pygame.image.load("sprites/start.png").convert_alpha()
        self.start_button = pygame.transform.scale(self.start_button_image, (100, 50))
        self.start_rect = self.start_button.get_rect()
        self.start_rect.center = (DISPLAY[0] / 2, 500)

        self.instructions_image = pygame.image.load("sprites/instructions.png").convert_alpha()
        self.instructions = pygame.transform.scale(self.instructions_image, (200, 150))
        self.instructions_rect = self.instructions.get_rect()
        self.instructions_rect.center = (DISPLAY[0] / 2, 600)

        background = pygame.image.load("catching_fish.png").convert()
        self.background = pygame.transform.scale(background, WINDOW)
        self.back_rect = self.background.get_rect()
        self.back_rect.topleft = (0,0)

        self.run = True

    def run_menu(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.start_rect.collidepoint(pos):
                        self.run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.run = False
            self.screen.blit(self.background, self.back_rect)
            self.screen.blit(self.start_button, self.start_rect)
            self.screen.blit(self.instructions, self.instructions_rect)

            pygame.display.update()
    
    def getState(self):
        return self.run