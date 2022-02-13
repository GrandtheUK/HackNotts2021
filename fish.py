import random
import fish_data

class Fish:
    def __init__(self):
        """Takes in min and max size of fish in a tuple (min, max)"""
        self.type = self.createType()
        self.fish = fish_data.fish[self.type]
        self.size = random.randint(self.fish["size"][0],self.fish["size"][1])
        self.weight = random.randint(self.fish["weight"][0],self.fish["weight"][1])
        self.energy = 100
        self.recoveryRate = random.randint(self.fish["recovery"][0],self.fish["recovery"][1])
        self.recoveryCounter = 0

    
    def recover(self):
        self.recoveryCounter += 1
        if self.recoveryCounter > 5:
            self.recoveryRate = random.randint(self.fish["recovery"][0],self.fish["recovery"][1])
            self.recoveryCounter = 0
        self.energy += self.recoveryRate
        if self.energy > 100:
            self.energy = 100

    def __repr__(self) -> str:
        return f"{self.type}, {self.weight}, {self.size}"

    def createType(self):
        prob = random.random()
        if prob < 0.05: return "Nemo"
        elif prob < 0.10: return "Magikarp"
        elif prob < 0.25: return "Dead fish"
        elif prob < 0.30: return "Shoe fish"
        elif prob < 0.45: return "Grayling"
        elif prob < 0.50: return "Brown Trout"
        elif prob < 0.65: return "Zander"
        elif prob < 0.75: return "Chub"
        elif prob < 0.9: return "Carp"
        else:
            num = random.randint(1, 2)
            match num:
                case 1: return "Shoe"
                case 2: return "Stick"

