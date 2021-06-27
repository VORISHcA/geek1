from random import randint
from timeit import timeit
from collections import deque


def l_append(lst):
    for i in range(100):
        lst.append(randint(1, 10000))


def d_append(deq):
    for i in range(100):
        deq.append(randint(1, 10000))


def l_begin(lst):
    for i in range(100):
        lst.insert(0, randint(1, 10000))


def d_begin(deq):
    for i in range(100):
        deq.appendleft(randint(1, 10000))


def l_pop(lst):
    for i in range(100):
        lst.pop()


def d_pop(deq):
    for i in range(100):
        deq.pop()


test1 = [randint(1, 10000) for el in range(1, 1000000)]
test2 = deque(test1)
print('в конец l', timeit("l_append(test1)", globals=globals(), number=10000))
print('в конец d', timeit("d_append(test2)", globals=globals(), number=10000))
print('в начало l', timeit("l_begin(test1)", globals=globals(), number=100))
print('в начало d', timeit("d_begin(test2)", globals=globals(), number=100))
print('удалениеи в l', timeit("l_pop(test1)", globals=globals(), number=1000))
print('удалениеи в d', timeit("d_pop(test2)", globals=globals(), number=1000))

# Вставка в конец не имеет никакой разницы по времени работы, но вставка в начало в 1000 раз быстрее
