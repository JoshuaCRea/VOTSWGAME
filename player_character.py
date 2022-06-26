from unicodedata import name
from config import HOMETOWNS

class PlayerCharacter:
    def __init__(self, name, hometown):
        self.hp = 5
        self.name = name
        self.standing = True
        self.injured = False
        self.STA = HOMETOWNS[hometown]["STA"]
        self.POW = HOMETOWNS[hometown]["POW"]
        self.AGI = HOMETOWNS[hometown]["AGI"]
        self.CHI = HOMETOWNS[hometown]["CHI"]
        self.WIT = HOMETOWNS[hometown]["WIT"]

    def receive_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.standing = False
            self.injured = True
    
