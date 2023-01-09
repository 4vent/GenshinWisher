from typing import Union
import shutil
from typing import Dict
import charactors as c
from wish import EventWish

# COST = 2     #    60 /    120 yen
# COST = 1.85  #   330 /    610 yen
# COST = 1.69  # 1,090 /  1,840 yen
# COST = 1.64  # 2,240 /  3,680 yen
# COST = 1.57  # 3,880 /  6,100 yen
COST = 1.49  # 8,080 / 12,000 yen


def main(cell_width=12, width: Union[int, None] = None):
    from eastasianwidth import ljust2, width2

    if width is None:
        width = shutil.get_terminal_size().columns

    pu5 = [c.Raiden_Shogun]
    pu4 = [c.Kujou_Sara, c.Sayu, c.Rosaria]
    wish = EventWish(pu5, pu4)  # type: ignore
    gems = 0

    hit_chars: Dict[c.Charactor, int] = {}
    while True:
        carsole = 0
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
            cell = ljust2(result.name, cell_width) + ' '
            print(ljust2(result.name, cell_width), end='')
            carsole += width2(cell)
            if carsole + cell_width > width:
                carsole = 0
                print('')
            print('\033[0m', end='')

            if isinstance(result, c.Charactor):
                if result not in hit_chars:
                    hit_chars[result] = -1
                hit_chars[result] += 1
        
        # for _ in range(pu4count):
        #     print('\033[38;5;045m*4PU\033[0m ', end='')
        # for _ in range(pu5count):ß
        #     print('\033[38;5;220m*5PU!\033[0m ', end='')

        carsole = 0
        
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

            cell = k.name + ':' + ('無' if v == 0 else str(v) if v < 6 else f'完({v})') + '凸 '
            print(ljust2(cell, cell_width), end='')
            print('\033[0m', end='')

            carsole += width2(cell)
            if carsole + cell_width > width:
                carsole = 0
                print('')
        
        if not input('\n') == '':
            break


if __name__ == "__main__":
    main()