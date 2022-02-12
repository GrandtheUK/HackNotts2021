import pygame
import sprite_sheet

class Fisherman(pygame.sprite.Sprite):
    spriteSheet = sprite_sheet.Spritesheet("fisherman.jpg", (1024,1325), (1,1))

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





class Tile(pygame.sprite.Sprite):
    spriteSheet = sprite_sheet.Spritesheet("sprites/background_sprites.png", (16,16), (4,5))
    def __init__(self, id, posx, posy, height, width) -> None:
        super().__init__()
        self.id = id
        self.posx = posx
        self.posy = posy
        self.height = height
        self.width = width
        img = self.spriteSheet.get_sprite_image(id)
        self.image = pygame.transform.scale(img, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.posx, self.posy)


