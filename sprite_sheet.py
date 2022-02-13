import pygame


class Spritesheet():
    def __init__(self, file, spriteDim, gridDim, startCoords=(0,0), colourKey=(0,0,0)):
        self.sheet = pygame.image.load(file)
        self.colourKey = colourKey
        self.spriteList = []
        for i in range(gridDim[0]):
            y = startCoords[1] + i * spriteDim[1]
            for j in range(gridDim[1]):
                x = startCoords[0] + j * spriteDim[0]
                sprite = pygame.Surface([spriteDim[0], spriteDim[1]])
                sprite.blit( self.sheet, (0,0), (x,y,spriteDim[0], spriteDim[1]) )
                sprite.set_colorkey(self.colourKey)
                self.spriteList.append(sprite)


    def get_sprite_image(self, id, flip=False):
        """Returns single image from spritesheet"""
        sprite = self.spriteList[id]
        if flip:
            sprite = pygame.transform.flip(sprite, True, False)
        return sprite
        
    def get_sprite_list(self, flip=False):
        """Returns tuple of all images in sequence for sprite"""
        animationList = [self.get_sprite_image(i,flip) for i,_ in enumerate(self.spriteList)]
        return animationList

