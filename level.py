import pygame, json

LEVELS = ["01-river"]

def loadLevel(levelName):#screen,gridSize,TILESIZE):
    with open("levels/" + levelName + ".json") as f:
        level = json.load(f)
    print(f"Loaded level \"{level['name']}\" correctly")
    
    return level

def getLevelData(levelName):
    levelData = loadLevel(levelName)
    data = levelData["data"]
    return data