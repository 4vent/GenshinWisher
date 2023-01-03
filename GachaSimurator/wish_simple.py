from tqdm import tqdm
from wish import Wish


COST = 1.49


def 基本ガチャシミュレーター():
    wish = Wish()
    while True:
        for _ in range(10):
            r = wish.wish()
            if r == 5:
                print('\033[38;5;130m5 \033[0m', end='')
            elif r == 4:
                print('\033[38;5;053m4 \033[0m', end='')
            elif r == 55:
                print('\033[38;5;220m5 \033[0m', end='')
            elif r == 44:
                print('\033[38;5;045m4 \033[0m', end='')
            else:
                print(str(r) + ' ', end='')
        if not input() == '':
            break


def ピックアップが出るまで回す():
    wish = Wish()
    attempt = 0
    sum = 0
    print('回数\t平均')
    while True:
        attempt += 1
        count = 0
        while True:
            count += 1
            if wish.wish() == 55:
                break
        sum += count
        print(str(count) + '\t' + str(sum / attempt), end='')
        if not input() == '':
            break


def ピックアップが出るまで回す2():
    wish = Wish()
    ATTEMPT = 10 ** 7 * 3
    sum = 0
    arr = [0] * 180
    for _ in tqdm(range(ATTEMPT)):
        count = 0
        while True:
            count += 1
            if wish.wish() == 55:
                break
        arr[count - 1] += 1

        sum += count
    
    i = 0
    with open('result.txt', 'w') as f:
        for _ in range(18):
            for __ in range(10):
                a = arr[i] / ATTEMPT
                f.write(str(a) + '\n')
                print(f'[{str(i+1).rjust(3)}] {a * 100:.5f}%\t', end='')
                i += 1
            print('')
    print(str(sum / ATTEMPT) + '回')


def 凸るまで回す(凸数: int = 6, histgram=False):
    wish = Wish()
    ATTEMPT = 10 ** 4

    sum_wishes = 0
    sum_fee = 0

    under20k = 0
    in20k40k = 0
    in40k60k = 0
    in60k80k = 0
    in80k100k = 0
    in100k120k = 0
    in120k140k = 0
    in140k160k = 0
    in160k180k = 0
    in180k200k = 0
    over200k = 0

    i = 0
    # f = open('result_凸るまで.csv', 'w')
    for _ in range(ATTEMPT):
        i += 1
        pucount = 0
        wishcount = 0
        while True:
            wishcount += 1
            if wish.wish() == 55:
                pucount += 1
                if pucount > 凸数:
                    break
        wishes = wishcount
        fee = wishcount * 160 * COST
        sum_wishes += wishes
        sum_fee += fee

        if fee < 2_0000:
            under20k += 1
        elif fee < 4_0000:
            in20k40k += 1
        elif fee < 6_0000:
            in40k60k += 1
        elif fee < 8_0000:
            in60k80k += 1
        elif fee < 10_0000:
            in80k100k += 1
        elif fee < 12_0000:
            in100k120k += 1
        elif fee < 14_0000:
            in120k140k += 1
        elif fee < 16_0000:
            in140k160k += 1
        elif fee < 18_0000:
            in160k180k += 1
        elif fee < 20_0000:
            in180k200k += 1
        else:
            over200k += 1
        # f.write(str(wishes) + '\n')
        print(f'{wishes}回\t{fee:,.0f}円 \t(avg. {sum_wishes / i:.2f}回\t{sum_fee / i:,.0f}円)', end='')
        if histgram:
            print(f'\t |0万| {under20k} |2| {in20k40k} |4| {in40k60k} |6| {in60k80k} |8| {in80k100k} |10| {in100k120k} |12| {in120k140k} |14| {in140k160k} |16| {in160k180k} |18| {in180k200k} |20| {over200k}', end='')
        if not input() == '':
            break
    # f.close()
    # print(f'{sum_wishes / ATTEMPT:.2f}回\t{sum_fee / ATTEMPT:,.0f}円')


# 基本ガチャシミュレーター()
# ピックアップが出るまで回す()
# ピックアップが出るまで回す2()
凸るまで回す(6, True)