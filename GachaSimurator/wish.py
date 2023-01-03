from random import choice, random
from typing import Union, List

import charactors as c
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
    char4: List[Union[c.Charactor, c.Weapon]] = []
    weapon4: List[Union[c.Charactor, c.Weapon]] = []
    pu4  : List[Union[c.Charactor, c.Weapon]] = []
    item5: List[Union[c.Charactor, c.Weapon]] = []
    pu5  : List[Union[c.Charactor, c.Weapon]] = []

    def __init__(self, pu5: Union[List[Union[c.Charactor, c.Weapon]], None] = None,
                 pu4: Union[List[Union[c.Charactor, c.Weapon]], None] = None,) -> None:
        if pu5 is None:
            self.nopu5 = True
        else:
            self.nopu5 = False
            self.pu5 = pu5
        if pu4 is None:
            self.nopu4 = True
        else:
            self.nopu4 = False
            self.pu4 = pu4
        
        super().__init__()

    def wish(self):
        result = super().wish()
        if result == 44:
            if self.nopu4:
                if random() < 0.147305389:
                    return choice(self.char4)
                else:
                    return choice(self.weapon4)
            else:
                return choice(self.pu4)
        elif result == 4:
            while True:
                if random() < 0.147305389:
                    r = choice(self.char4)
                else:
                    r = choice(self.weapon4)
                if r not in self.pu4:
                    return r
        if result == 55:
            if self.nopu5:
                return choice(self.item5)
            else:
                return choice(self.pu5)
        elif result == 5:
            while True:
                r = choice(self.item5)
                if r not in self.pu5:
                    return r
        else:
            return c.Weapon('*3', 3)


class EventWish(WishFull):
    char4: List[Union[c.Charactor, c.Weapon]] = [
        c.Fischl, c.Barbara, c.Xiangling, c.Xingqiu, c.Sucrose, c.Noelle,
        c.Ningguang, c.Diona, c.Beidou, c.Chongyun, c.Xinyan, c.Razor,
        c.Bennett, c.Rosaria, c.Yanfei, c.Sayu, c.Kujou_Sara, c.Thoma,
        c.Gorou, c.Yun_Jin, c.Kuki_Shinobu, c.Shikanoin_Heizou, c.Collei,
    ]
    weapon4 = [
        c.Weapon('武器1', 4), c.Weapon('武器2', 4), c.Weapon('武器3', 4),
        c.Weapon('武器4', 4), c.Weapon('武器5', 4), c.Weapon('武器6', 4),
        c.Weapon('武器7', 4), c.Weapon('武器8', 4), c.Weapon('武器9', 4),
        c.Weapon('武器10', 4), c.Weapon('武器11', 4), c.Weapon('武器12', 4),
        c.Weapon('武器13', 4), c.Weapon('武器14', 4), c.Weapon('武器15', 4),
        c.Weapon('武器16', 4), c.Weapon('武器17', 4), c.Weapon('武器18', 4),
    ]
    item5: List[Union[c.Charactor, c.Weapon]] = [
        c.Jean, c.Diluc, c.Mona, c.Qiqi, c.Keqing, c.Tighnari,
    ]