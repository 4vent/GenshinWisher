from typing import Dict
import charactors as c
from wish import EventWish

# COST = 2     #    60 /    120 yen
# COST = 1.85  #   330 /    610 yen
# COST = 1.69  # 1,090 /  1,840 yen
# COST = 1.64  # 2,240 /  3,680 yen
# COST = 1.57  # 3,880 /  6,100 yen
COST = 1.49  # 8,080 / 12,000 yen


def main(ljust_width=18):
    from ljust_eastasianwidth import ljust2

    pu5 = [c.Raiden_Shogun]
    pu4 = [c.Kujou_Sara, c.Sayu, c.Rosaria]
    wish = EventWish(pu5, pu4)  # type: ignore
    gems = 0

    hit_chars: Dict[c.Charactor, int] = {}
    while True:
        pu4count = 0
        pu5count = 0
        gems += 1600
        print(f"¥{gems * COST:,.0f} / {gems:,} gems")
        for i in range(10):
            result = wish.wish()
            if result.rarity == 5:
                if result in pu5:
                    pu5count += 1
                    print('\033[38;5;220m', end='')
                else:
                    print('\033[38;5;130m', end='')
            elif result.rarity == 4:
                if result in pu4:
                    pu4count += 1
                    print('\033[38;5;045m', end='')
                else:
                    print('\033[38;5;053m', end='')
            print(ljust2(result.name, ljust_width), end=' ')
            if i == 4:
                print('')
            print('\033[0m', end='')

            if isinstance(result, c.Charactor):
                if result not in hit_chars:
                    hit_chars[result] = -1
                hit_chars[result] += 1
        
        # for _ in range(pu4count):
        #     print('\033[38;5;045m*4PU\033[0m ', end='')
        # for _ in range(pu5count):
        #     print('\033[38;5;220m*5PU!\033[0m ', end='')
        
        print('')
        for k, v in hit_chars.items():
            if k.rarity == 5:
                if k in pu5:
                    pu5count += 1
                    print('\033[38;5;220m', end='')
                else:
                    print('\033[38;5;130m', end='')
            elif k.rarity == 4:
                if k in pu4:
                    pu4count += 1
                    print('\033[38;5;045m', end='')
                else:
                    print('\033[38;5;053m', end='')

            print(ljust2(k.name + ':' + ('無' if v == 0 else str(v) if v < 6 else f'完({v})') + '凸', ljust_width), end='\n')
            print('\033[0m', end='')
        
        if not input('\n') == '':
            break



if __name__ == "__main__":
    main(10)