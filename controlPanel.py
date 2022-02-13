import pygame, sprite_sheet
from config import DISPLAY
import os
from pygame import freetype

controlPanelColour = (127,127,10)
infographicColour = (180,180,20)

def open_diary():
    os.startfile("diary.txt")


class ControlPanel:
    def __init__(self, height, width, top, functions) -> None:
        self.image = pygame.Surface([width,height])
        pygame.draw.rect(self.image,controlPanelColour,pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
        self.top = top
        self.powerBar = PowerBar(height, ( width//2 - height//2 ,top))
        self.buttons = {
            "button1" :  Button(100,50,(0,top), functions["exit"], "sprites/button_exit.png"),
            "button2" :  Button(100,50,(0,top + 50), open_diary, "sprites/button_scores.png")
        }
        self.angle = 0
        self.power = 0
        self.mode = 0
        self.angleIncrease = True
        self.lineBar = Bar(100,50,(DISPLAY[0]-200, top))
        self.fishBar = Bar(100,50,(DISPLAY[0]-50, top))
        self.lineBarIcon = BarImage(100,100,(DISPLAY[0]-300, top), "sprites/line_strength.png")
        self.fishBarIcon = BarImage(100,100,(DISPLAY[0]-150, top), "sprites/fish_strength.png")
        self.lineBarVal = 0
        self.fishBarVal = 0
        self.infographic = Infographic(90, 200, (105,top + 5))
        self.lastFish = None
        
        
    def draw(self, screen):
        pygame.Surface.blit(screen, self.image, (0,self.top))
        self.powerBar.draw(screen)
        self.lineBar.draw(screen)
        self.fishBar.draw(screen)
        self.lineBarIcon.draw(screen)
        self.fishBarIcon.draw(screen)
        self.infographic.draw(screen, self.lastFish)
        for button in self.buttons.values():
            button.draw(screen)

    def update(self):
        if self.mode == 0:
            if self.angleIncrease:
                self.angle += 1
                if self.angle > 45:
                    self.angle = 45
                    self.angleIncrease = False
            else:
                self.angle -= 1
                if self.angle < -45:
                    self.angle = -45
                    self.angleIncrease = True
        elif self.mode == 1:
            self.power += 1
            if self.power > 100:
                self.power = 0
        angle = self.angle + 45
        self.powerBar.angleBar = angle // (90 / 7)
        powerBar = self.power // (100 / 8)
        if powerBar > 7:
            powerBar = 7
        self.powerBar.powerBar = powerBar

        lineBar = self.lineBarVal // (100 / 8)
        if lineBar > 7:
            lineBar = 7
        lineBar = 7 - int(lineBar)
        self.lineBar.barValue = int(lineBar)

        fishBar = self.fishBarVal // (100 / 8)
        if fishBar > 7:
            fishBar = 7
        if fishBar < 0:
            fishBar = 0
        self.fishBar.barValue = int(fishBar)
        

    def check_cursor_pos(self, mousepos):
        for button in self.buttons.values():
            if button.rect.collidepoint(mousepos):
                button.performFunction()


class Infographic:
    bigfish = sprite_sheet.Spritesheet("sprites/big_fish.png", (32,16), (4,1))
    smallfish = sprite_sheet.Spritesheet("sprites/small_fish_and_trash.png", (16,16), (3,3))
    def __init__(self, height, width, topleft) -> None:
        self.image = pygame.Surface([width,height])
        pygame.draw.rect(self.image, infographicColour, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
        self.topleft = topleft

    @staticmethod
    def get_fish_id(fish):
        fishNames = {
        "Nemo" : (1,2),
        "Magikarp" : (0,3),
        "Dead fish" : (1,6),
        "Shoe fish" : (1,5),
        "Grayling" : (1,4),
        "Brown Trout" : (0,2),
        "Zander" : (0,1),
        "Chub" : (1,3),
        "Carp" : (0,0),
        "Shoe" : (1,0),
        "Stick" : (1,1)
        }
        return fishNames[fish]


    def draw(self, screen, lastFish):
        pygame.Surface.blit(screen, self.image, self.topleft)
        if lastFish == "line-snap":
            font = pygame.font.Font('Pokemon GB.ttf', 16)
            lineErr = font.render("Line Snapped!", True, (0,0,0))
            lineErrRect = lineErr.get_rect()
            lineErrRect.topleft = (self.topleft[0]+30, self.topleft[1] + 40)
            pygame.Surface.blit(screen, lineErr, lineErrRect)  
        elif lastFish is not None:
            fishId = self.get_fish_id(lastFish.type)
            if fishId[0] == 0:
                img = self.bigfish.get_sprite_image(fishId[1])
            else:
                img = self.smallfish.get_sprite_image(fishId[1])
            image = pygame.transform.scale(img, (100-fishId[0]*50, 50))
            pygame.Surface.blit(screen, image, (self.topleft[0]+5+fishId[0]*25,self.topleft[1]+25))

            font = pygame.font.Font('Pokemon GB.ttf', 12)
        
            title = font.render(lastFish.type, True, (0,0,0))
            titleRect = title.get_rect()
            titleRect.topleft = (self.topleft[0]+110, self.topleft[1] + 20)
            pygame.Surface.blit(screen, title, titleRect)
            
            weightLabel = f"Weight: {lastFish.weight} lbs"
            weight = font.render(weightLabel, True, (0,0,0))
            weightRect = weight.get_rect()
            weightRect.topleft = (self.topleft[0]+110, self.topleft[1] + 40)
            pygame.Surface.blit(screen, weight, weightRect)
            
            sizeLabel = f"Size: {lastFish.size} inches"
            size = font.render(sizeLabel, True, (0,0,0))
            sizeRect = size.get_rect()
            sizeRect.topleft = (self.topleft[0]+110, self.topleft[1] + 60)
            pygame.Surface.blit(screen, size, sizeRect)
    

class Bar:
    spriteSheet = sprite_sheet.Spritesheet("sprites/fish_bar.png", (16,32), (2,4))
    def __init__(self, height, width, topleft) -> None:
        self.height = height
        self.width = width
        img = self.spriteSheet.get_sprite_image(0)
        self.animationList = self.spriteSheet.get_sprite_list()
        self.image = pygame.transform.scale(img, (width,height))
        self.rect = self.image.get_rect()
        self.topleft = topleft
        self.barValue = 0
            
    def draw(self, screen):
        img = self.animationList[self.barValue]
        self.image = pygame.transform.scale(img, (self.width,self.height))
        pygame.Surface.blit(screen, self.image, self.topleft)

class BarImage:
    def __init__(self, height, width, topleft, path) -> None:
        self.height = height
        self.width = width
        img = pygame.image.load(path)
        self.image = pygame.transform.scale(img, (width,height))
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft
        self.topleft = topleft

    def draw(self, screen):
        pygame.Surface.blit(screen, self.image, self.topleft)

class Button:
    def __init__(self, width, height, topleft, buttonFunction=None, path="sprites/button.png") -> None:
        img = pygame.image.load(path)
        self.image = pygame.transform.scale(img, (width,height))
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft
        self.topleft = topleft
        self.buttonFunction = buttonFunction
    
    def draw(self, screen):
        pygame.Surface.blit(screen, self.image, self.topleft)
    
    def performFunction(self):
        self.buttonFunction()




class PowerBar:
    spriteSheet = sprite_sheet.Spritesheet("sprites/power_bar.png", (32,32), (8,7), (32,0))
    def __init__(self, dim, topleft) -> None:
        self.dim = dim
        img = self.spriteSheet.get_sprite_image(0)
        self.animationList = self.spriteSheet.get_sprite_list()
        self.image = pygame.transform.scale(img, (dim,dim))
        self.rect = self.image.get_rect()
        self.topleft = topleft
        self.angleBar = 0
        self.powerBar = 0
        self.lineBar = 0
        self.fishBar = 0
    
    def draw(self, screen):
        imgIndex = int(self.powerBar * 7 + self.angleBar)
        img = self.animationList[imgIndex]
        self.image = pygame.transform.scale(img, (self.dim,self.dim))
        pygame.Surface.blit(screen, self.image, self.topleft)