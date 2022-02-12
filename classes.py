import pygame
import sprite_sheet

class Fisherman(pygame.sprite.Sprite):
    spriteSheet = sprite_sheet.Spritesheet("sprites/player_tall.png", (16,32), (1,1))

    def __init__(self, posx, posy, width, height, spriteGroup) -> None:
        super().__init__()
        self.posx = posx
        self.posy = posy
        self.height = height
        self.width = width
        img = self.spriteSheet.get_sprite_image(0)
        self.image = pygame.transform.scale(img, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.posx, self.posy)
        self.float = None
        self.spriteGroup = spriteGroup
        self.state = "standing"
        self.castCounter = 0
    
    def cast(self):
        self.state = "casting"
        self.float = Float(self.spriteGroup, (self.posx, self.posy))

    def update(self):
        if self.state == "casting":
            self.float.move(-5,-5)
            self.castCounter += 1
            if self.castCounter == 30:
                self.state = "standing"
                self.castCounter = 0
                self.float.inWater = True



class Float(pygame.sprite.Sprite):
    spriteSheet = sprite_sheet.Spritesheet("sprites/bobber.png", (16,16), (1,4))
    def __init__(self, spriteGroup, pos) -> None:
        super().__init__()
        img = self.spriteSheet.get_sprite_image(0)
        self.animationList = self.spriteSheet.get_sprite_list()
        self.image = pygame.transform.scale(img, (50, 50))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        spriteGroup.add(self)
        self.inWater = False
        self.animationTicks = 0
        self.animationCounter = 1

    def move(self, movex, movey):
        self.rect.center = (self.rect.center[0] + movex, self.rect.center[1] + movey)
    
    def update(self):
        if self.inWater:
            if pygame.time.get_ticks() > self.animationTicks + 200:
                self.animationTicks = pygame.time.get_ticks()
                self.animationCounter += 1
                if self.animationCounter >= len(self.animationList):
                    self.animationCounter = 1
                img = self.spriteSheet.get_sprite_image(self.animationCounter)
                self.image = pygame.transform.scale(img, (50, 50))


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


class Line:
    def __init__(self, screen, startPos, endPos) -> None:
       self.startPos = startPos
       self.endPos = endPos
       self.screen = screen

    def update(self, showLine = False):
        if showLine:
            pygame.draw.line(self.screen, (0,0,0), self.startPos, self.endPos)

    def set_endPos(self, pos):
        self.endPos = pos

    def set_startPos(self, pos):
        self.startPos = pos