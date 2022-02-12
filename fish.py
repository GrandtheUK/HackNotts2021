import random

class Fish:
    def __init__(self, size):
        """Takes in min and max size of fish in a tuple (min, max)"""
        self.type = self.getType()
        self.size = self.size(size)
        self.weight = self.setWeight()

    def setWeight(self):
        if self.type == "Carp":
            return round(random.uniform(0.5, 4.0), 2)
        if self.type == "Chub":
            return round(random.uniform(0.5, 8.0), 2)
        if self.type == "Zander":
            return round(random.uniform(1.0, 11.0), 2)
        if self.type == "Brown Trout":
            return round(random.uniform(3.0, 20.0), 2)
        if self.type == "Grayling":
            return round(random.random(1.0, 6.7), 2)
        if self.type == "Shoe fish":
            return round(random.random())

    
    def size(self, size):
        s = random.randint(size[0], size[1])
        return s

    def getType(self):
        prob = random.random()

        if prob < 0.5: return "Carp"
        elif prob < 0.40: return "Chub"
        elif prob < 0.35: return "Zander"
        elif prob < 0.30: return "Brown Trout"
        elif prob < 0.25: return "Grayling"
        elif prob < 0.20: return "Shoe fish"
        elif prob < 0.15: return "Dead fish"
        elif prob < 0.10: return "Tiny fin"
        elif prob < 0.05: return "Nemo"
        else:
            num = random.randint(1, 4)

            match num:
                case 1: return "Shoe"
                case 2: return "Stick"
                case 3: return "Rusty knife"
                case 4: return "Exploded battery"

