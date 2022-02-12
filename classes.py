import pygame
import sprite_sheet

class Fisherman(pygame.sprite.Sprite):
    spriteSheet = sprite_sheet.Spritesheet("fisherman.jpg", (100,100), (3,3))
    print(spriteSheet.get_sprite_list())

    def __init__(self, posx, posy, height, width) -> None:
        super().__init__()
        self.posx = posx
        self.posy = posy
        self.height = height
        self.width = width
        img = self.spriteSheet.get_sprite_image(0)
        self.image = pygame.transform.scale(img, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.posx, self.posy)


