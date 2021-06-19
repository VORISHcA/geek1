from random import randint
from timeit import default_timer

"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и укажите дала ли оптимизация эффективность.
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""


def time_it(func):
    def show(numb):
        first_time = default_timer()
        func(numb)
        print(default_timer() - first_time)

    return show


@time_it
def bubble(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


@time_it
def new_bubble(lst):
    for i in range(len(lst) - 1):
        end_sort = True
        for j in range(len(lst) - i - 1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                end_sort = False
        if end_sort:
            break


new_list = [randint(-100, 100) for i in range(10000)]
bubble(new_list)
new_list = [randint(-100, 100) for i in range(10000)]
new_bubble(new_list)
new_bubble(new_list)


'''
В теории в ситуации, где большая часть уже осортирована, оптимизированная сортировка
должна показывать себя лучше, но примерно за 10 запусков, обычная сортировка справлялась за меньшее время
Зато с уже осортированным список отлично 
8.310103
8.4073726
0.0008955999999997744
'''