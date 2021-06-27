from random import randint
from timeit import timeit
from collections import OrderedDict


def d_filling(dct):
    for i in range(10000):
        dct[i] = randint(1, 5000)
    return dct


def di_filling(dct):
    o_dct = OrderedDict(dct.items())
    return o_dct


def get_dict(dct):
    for i in range(1000):
        res = dct[randint(0, 4999)]


def get_orde(o_dct):
    for i in range(1000):
        res = o_dct[randint(0, 4999)]


dct = {}
dct = d_filling(dct)
o_dct = di_filling(dct)

print('заполнение словаря', timeit("d_filling(dct)", globals=globals(), number=100))
print('Заполнение OrderedDict', timeit("di_filling(o_dct)", globals=globals(), number=100))
print('Элемент по номеру', timeit("get_dict(dct)", globals=globals(), number=1000))
print('Элемент по номеру в OrderedDict', timeit("get_orde", globals=globals(), number=1000))

# Создавать упорядоченный из простого все равно время, но получение случайного элемента в упорядоченном у меня заняло 1.1800000000228295e-05,
# что во много раз быстрее
