import pygame, sprite_sheet
from config import DISPLAY

controlPanelColour = (127,127,10)


def test_function():
    print("test")

def test_function2():
    print("test2")


class ControlPanel:
    def __init__(self, height, width, top, functions) -> None:
        self.image = pygame.Surface([width,height])
        pygame.draw.rect(self.image,controlPanelColour,pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
        self.top = top
        self.powerBar = PowerBar(height, ( width//2 - height//2 ,top))
        self.buttons = {
            "button1" :  Button(100,50,(0,top), test_function),
            "button2" :  Button(100,50,(0,top + 50), test_function2),
            "reelButton" :  Button(100,50, (DISPLAY[0] - 100,top + 50), functions["reel_in"])
        }
        self.angle = 0
        self.power = 0

        
    def draw(self, screen):
        pygame.Surface.blit(screen, self.image, (0,self.top))
        self.powerBar.draw(screen)
        for button in self.buttons.values():
            button.draw(screen)

    def update(self):
        pass

    def check_cursor_pos(self, mousepos):
        for button in self.buttons.values():
            if button.rect.collidepoint(mousepos):
                button.performFunction()


class PowerBar:
    spriteSheet = sprite_sheet.Spritesheet("sprites/power_bar.png", (32,32), (1,1))
    def __init__(self, dim, topleft) -> None:
        img = self.spriteSheet.get_sprite_image(0)
        self.image = pygame.transform.scale(img, (dim,dim))
        self.rect = self.image.get_rect()
        self.topleft = topleft
    
    def draw(self, screen):
        pygame.Surface.blit(screen, self.image, self.topleft)


class Button:
    def __init__(self, width, height, topleft, buttonFunction=None) -> None:
        img = pygame.image.load("R.png")
        self.image = pygame.transform.scale(img, (width,height))
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft
        self.topleft = topleft
        self.buttonFunction = buttonFunction
    
    def draw(self, screen):
        pygame.Surface.blit(screen, self.image, self.topleft)
    
    def performFunction(self):
        self.buttonFunction()