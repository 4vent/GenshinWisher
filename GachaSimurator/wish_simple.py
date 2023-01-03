from tqdm import tqdm
from GachaSimurator.wish import Wish


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


基本ガチャシミュレーター()
# ピックアップが出るまで回す()
# ピックアップが出るまで回す2()