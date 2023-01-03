from random import random
import colord_pythonista
colord_pythonista.setup()


RATE4 = 0.051
RATE4UP = 0.511
RATE5 = 0.006
RATE5UP = 0.324


class Wish():
    def __init__(self) -> None:
        self.count4 = 0
        self.count5 = 0
        self.compassion4 = False
        self.compassion5 = False
    
    def wish(self):
        rarity = self.get_rarity()
        if rarity == 4:
            if self.compassion4 or random() < 0.5:
                self.compassion4 = False
                return 44
            else:
                self.compassion4 = True
                return 4
        elif rarity == 5:
            if self.compassion5 or random() < 0.5:
                self.compassion5 = False
                return 55
            else:
                self.compassion5 = True
                return 5
        else:
            return rarity
    
    def get_rarity(self):
        self.set_th()

        th = random()
        if th < self.th5:
            self.count4 += 1
            self.count5 = 0
            return 5
        elif th < self.th4:
            self.count4 = 0
            self.count5 += 1
            return 4
        else:
            self.count4 += 1
            self.count5 += 1
            return 3
    
    def set_th(self):
        if self.count5 < 75:
            self.th5 = RATE5
        elif self.count5 < 89:
            self.th5 = RATE5UP
        else:
            self.th5 = 1
        
        if self.count4 < 8:
            self.th4 = self.th5 + RATE4
        elif self.count4 < 9:
            self.th4 = self.th5 + RATE4UP
        else:
            self.th4 = 1


class WishFull(Wish):
    characters = [
        
    ]
    def wish(self):
        return super().wish()