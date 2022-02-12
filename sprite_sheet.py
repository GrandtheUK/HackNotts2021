import pygame
import spriteSheet_meta


class Spritesheet():
    def __init__(self, file, colourKey=(0,0,0)):
        self.sheet = pygame.image.load(file)
        self.colourKey = colourKey

    def get_sprite_image(self, name, id, flip=False):
        """Returns single image from spritesheet"""
        spriteDimensions = spriteSheet_meta.get_sprite(name, id)
        sprite = pygame.Surface([spriteDimensions[2], spriteDimensions[3]])
        sprite.blit( self.sheet, (0,0), spriteDimensions )
        if flip:
            sprite = pygame.transform.flip(sprite, False, True)
        sprite.set_colorkey(self.colourKey)
        return sprite
        
    def get_animation_list(self, name, flipX=False):
        """Returns tuple of all images in sequence for sprite"""
        animationList = [self.get_sprite_image(name,i,flipX) for i,_ in enumerate(spriteSheet_meta.sprites[name])]
        return animationList


