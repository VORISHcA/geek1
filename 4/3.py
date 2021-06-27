def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    return ''.join(reversed(str(enter_num)))

import cProfile
import timeit


def main():
    print(f'revers_1 - {timeit.timeit("revers_1(123456)", globals=globals(), number=1000)} сек.')
    print(f'revers_2 - {timeit.timeit("revers_2(123456)", globals=globals(), number=1000)} сек.')
    print(f'revers_3 - {timeit.timeit("revers_3(123456)", globals=globals(), number=1000)} сек.')
    print(f'revers_4 - {timeit.timeit("revers_4(123456)", globals=globals(), number=1000)} сек.')


cProfile.run('main()')

#cProfile и timeit дали одинаковые результаты. Срез->reversed->цикл->рекурсия.