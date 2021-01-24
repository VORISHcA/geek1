import random
import numpy


class Card:
    def __init__(self, name):
        self.name = name

    def create_card(self):
        hard = list(numpy.random.permutation(numpy.arange(0, 100))[:15])
        cards = [[hard[j + 5 * i] for j in range(5)] for i in range(3)]
        for el in cards:
            for i in range(0,4):
                el.insert(random.randint(0, len(el)), '-')
        return cards


def print_matr(matr):
    print('---')
    for str in matr:
        print(*str)
    print('---')


class Game:
    @staticmethod
    def start_game(other1, other2, name1, name2):
        count_player = 0
        count_computer = 0
        choice = ''
        barrel = [i for i in range(1, 100)]
        random.shuffle(barrel)
        now_barrel = 0
        end = True
        while count_player != 15 and count_computer != 15 and choice != 's' and end:
            print(f'Ходит {name1}')
            print_matr(other2)
            print(f'Ходит {name2}')
            print_matr(other1)
            now_count = barrel[now_barrel]
            print(f'Сейчас выпало {now_count}')
            for str in other2:
                try:
                    str[str.index(now_count)] = '-'
                    count_computer += 1
                except:
                    pass

            choice = input('Введите y/n/s')
            in_str = False
            for str in other1:
                try:
                    str[str.index(now_count)] = '-'
                    in_str = True
                except:
                    pass
            if in_str and choice == 'y':
                count_player += 1
            elif in_str and choice == 'n':
                print('Вы проиграли')
                end = False
            elif in_str and choice == 'y':
                print('Вы проиграли')
                end = False

            now_barrel += 1
        if not end and count_player > count_computer:
            print(f'С победой! {count_player} {count_computer}')
        else:
            print(f'Вы проиграли со счетом {count_player} {count_computer}')


test = Card('Копьютер')
test2 = Card('Игрок')
Game.start_game(test.create_card(), test2.create_card(), test.name, test2.name)
lul = test.create_card()






