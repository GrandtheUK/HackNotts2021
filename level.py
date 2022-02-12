import json

LEVELS = ["01-river"]

def loadLevel(levelName):
    try:
        with open(f"levels/{levelName}.json") as f:
            level = json.load(f)
        print(f"Loaded level \"{level['name']}\" correctly")
    except:
        print(f"Unable to load file: {levelName}.json")
    
    return level

def getLevelData(levelName):
    levelData = loadLevel(levelName)
    data = levelData["data"]
    return data