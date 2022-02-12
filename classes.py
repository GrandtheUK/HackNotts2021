from extra_funcs import rand_with_step
import pygame, sprite_sheet
from random import randint, randrange, uniform
import fish
from config import *

class Fisherman(pygame.sprite.Sprite):
    spriteSheet = sprite_sheet.Spritesheet("sprites/player_sprites.png", (16,32), (1,1))

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
        self.hookedFish = False
        self.checkCatchCounter = 0
        self.catchMultiplier = 1
        self.castingAnimationCounter = 0
        self.castingAnimationTicks = 0
    
    def cast(self):
        self.state = "casting"
        self.float = Float(self.spriteGroup, self)
        self.float.move((350,200))
    
    def reel(self):
        self.state = "reeling"
        self.float.state = "reeling"
        self.float.target = self.rect.midtop

    def update(self):
        if self.float:
            if self.float.state == "inWater" and self.checkCatchCounter < pygame.time.get_ticks() and not self.float.caughtFish:
                self.checkCatchCounter = pygame.time.get_ticks() + (MINIMUM_CATCH_CHANCE * 1000)
                finalCatchChance = FISH_CATCH_CHANCE * self.catchMultiplier
                if rand_with_step(0, finalCatchChance, 0.125) == 1:
                    print("fish caught")
                    self.hookedFish = fish.Fish((1,20))
                    self.state = "caughtFish"
                    self.float.caughtFish = True
        
        # if pygame.time.get_ticks() > self.animationTicks + 200:
        #         self.animationTicks = pygame.time.get_ticks()
        #         self.animationCounter += 1
        #         if self.animationCounter >= len(self.animationList):
        #             self.animationCounter = 1
        #         img = self.animationList[self.animationCounter]
        #         self.image = pygame.transform.scale(img, (50, 50))



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
        self.caughtFish = False
        self.collisionRect = pygame.Rect(0, 0, self.rect.width * 0.2, self.rect.height * 0.2)
        self.collisionRect.center = self.rect.center

    def move(self, coords):
        self.target = coords

    
    def update(self):
        # keep collision rect inline with rect
        self.collisionRect.center = self.rect.center

        if self.caughtFish:
            for tile in Tile.landTiles:
                if self.collisionRect.colliderect(tile.rect):
                    vector = pygame.Vector2(self.rect.center) - pygame.Vector2(tile.rect.center)
                    self.target = self.pos + vector
        
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
                    self.fisherman.state = "standing"
                elif self.state == "reeling":
                    self.fisherman.float = None
                    self.kill()
                    return
            self.rect.center = self.pos
        else:
            if self.caughtFish:
                x = randint(0, DISPLAY[0])
                y = randint(0, DISPLAY[1])
                self.target = (x,y)


class Tile(pygame.sprite.Sprite):
    waterTiles = []
    landTiles = []
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
        if id == 0:
            self.waterTiles.append(self)
        else:
            self.landTiles.append(self)


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