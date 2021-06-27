from memory_profiler import memory_usage
from timeit import default_timer
from random import randint


def memory_time_profiler(func):
    def wrapper(*args, **kwargs):
        t1 = default_timer()
        mem1 = memory_usage()
        res = func(*args, **kwargs)
        mem2 = memory_usage()
        t2 = default_timer()
        print(f'Время выполнения {func.__name__}: {t2 - t1}\nИспользуемая память: {mem2[0] - mem1[0]} MiB')
        return res

    return wrapper


my_list = [randint(0, 1000) for i in range(30000)]


@memory_time_profiler
def loop_func(num):
    num_lst = list(range(num))
    for i in num_lst:
        return i


@memory_time_profiler
def gen_func(num):
    num_lst = list(range(num))
    for i in num_lst:
        yield i


loop_func(100000000)
gen_func(100000000)


@memory_time_profiler
def number_revers(num):
    if num == 0:
        return ' Перевернулось'
    else:
        revers = str(num % 10)
        num //= 10
        return revers + number_revers(num)


@memory_time_profiler
def number_revers_y(num):
    if num == 0:
        return ' Перевернулось'
    else:
        revers = str(num % 10)
        num //= 10
        yield revers + number_revers(num)


number_revers(234234)
number_revers_y(234234)
