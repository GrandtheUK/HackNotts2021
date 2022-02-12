


sprites = {
    "fisherman standing" : {
        0 : (50,50,500,500),
        1 : (70,70,500,500),
        2 : (80,80,500,500)
    },
    "fisherman catching" : {
        0 : (50,50,500,500),
        1 : (70,70,500,500),
        2 : (80,80,500,500)
    }
}

def get_sprite(name, id):
    """Returns sheet coordinates and size of sprite image"""
    return sprites[name][id]