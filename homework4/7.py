from itertools import count
from math import factorial


def fact(n):
    yield [factorial(el) for el in range(0, n)]


gen = fact
x = 20
for i in gen(x):
    print(i)
