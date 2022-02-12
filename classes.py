import pygame
import sprite_sheet

class Fisherman(pygame.sprite.Sprite):
    spriteSheet = sprite_sheet.Spritesheet("fisherman.jpg")

    animations = {
        "standing" : spriteSheet.get_animation_list("fisherman standing"),
        "catching" : spriteSheet.get_animation_list("fisherman catching")
    }

    def __init__(self, posx, posy, height, width) -> None:
        super().__init__()
        self.posx = posx
        self.posy = posy
        self.height = height
        self.width = width
        img = self.spriteSheet.get_sprite_image("fisherman standing", 0)
        self.image = pygame.transform.scale(img, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.posx, self.posy)
