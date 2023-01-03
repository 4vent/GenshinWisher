from random import random

from tqdm import tqdm


RATE4 = 0.051
RATE4UP = 0.511
RATE5 = 0.006
RATE5UP = 0.324


class Wish():
    def __init__(self) -> None:
        self.count4 = 0
        self.count5 = 0
    
    def wish(self):
        return self.get_rarity()
    
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


def main():
    wish = Wish()
    count5 = 0
    count4 = 0

    COUNT = 10 ** 8
    for _ in tqdm(range(COUNT)):
        result = wish.wish()
        if result == 5:
            count5 += 1
        elif result == 4:
            count4 += 1

    print('★4: ' + str(count4 * 100 / COUNT) + '%')
    print('★5: ' + str(count5 * 100 / COUNT) + '%')


def main1():
    wish = Wish()
    while True:
        for _ in range(10):
            r = wish.wish()
            if r == 5:
                print('\033[33m5 \033[0m', end='')
            elif r == 4:
                print('\033[35m4 \033[0m', end='')
            else:
                print(str(r) + ' ', end='')
        if not input() == '':
            break


main1()