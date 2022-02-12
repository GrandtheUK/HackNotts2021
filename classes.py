import pygame

class Fisherman(pygame.sprite.Sprite):
    def __init__(self, posx, posy, height, width) -> None:
        self.posx = posx
        self.posy = posy
        self.height = height
        self.width = width
        img = pygame.image.load("fisherman.jpg")
        self.image = pygame.transform.scale(img, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.center = (self.posx, self.posy)