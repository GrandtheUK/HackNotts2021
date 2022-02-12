import pygame
from config import BOBBER_TRAVEL_SPEED
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
        self.float = Float(self.spriteGroup, self)
        self.float.move((200,200))
    
    def reel(self):
        self.state = "reeling"
        self.float.state = "reeling"
        self.float.target = self.rect.midtop

    def update(self):
        pass
        # if self.state == "casting":
        #     self.float.move(-5,-5)
        #     self.castCounter += 1
        #     if self.castCounter == 30:
        #         self.state = "standing"
        #         self.castCounter = 0
        #         self.float.inWater = True
        # if self.state == "reeling":
        #     pass


class Float(pygame.sprite.Sprite):
    spriteSheet = sprite_sheet.Spritesheet("sprites/bobber_sprites.png", (16,16), (1,4))
    def __init__(self, spriteGroup, fisherman) -> None:
        super().__init__()
        self.fisherman = fisherman
        self.animationList = self.spriteSheet.get_sprite_list()
        img = self.animationList[0]
        self.image = pygame.transform.scale(img, (50, 50))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = fisherman.rect.midtop
        spriteGroup.add(self)
        self.state = "casting"
        self.animationTicks = 0
        self.animationCounter = 1
        self.pos = fisherman.rect.midtop
        self.target = fisherman.rect.midtop

    def move(self, coords):
        self.target = coords
    
    def update(self):
        speed = 1
        if self.state == "inWater":
            if pygame.time.get_ticks() > self.animationTicks + 200:
                self.animationTicks = pygame.time.get_ticks()
                self.animationCounter += 1
                if self.animationCounter >= len(self.animationList):
                    self.animationCounter = 1
                img = self.animationList[self.animationCounter]
                self.image = pygame.transform.scale(img, (50, 50))
        elif self.state == "casting":
            speed = 3
        elif self.state == "reeling":
            img = self.animationList[0]
            self.image = pygame.transform.scale(img, (50, 50))

        if self.target != self.pos:
            vector = pygame.Vector2(self.target) - pygame.Vector2(self.pos)
            vectorLen = vector.length()
            if vectorLen != 0:
                vector.normalize_ip()
                movement = vector * BOBBER_TRAVEL_SPEED * speed
                self.pos += movement
            if vectorLen < BOBBER_TRAVEL_SPEED * speed:
                self.pos = self.target
                if self.state == "casting":
                    self.state = "inWater"
                elif self.state == "reeling":
                    self.fisherman.float = None
                    self.kill()
                    return
            self.rect.center = self.pos


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