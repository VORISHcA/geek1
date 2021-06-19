"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти).
И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...
Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import random
import timeit


def merge_sort(a):
    n = len(a)
    if n < 2:
        return a

    left = merge_sort(a[:n//2])
    right = merge_sort(a[n//2:n])

    i = j = 0
    res = []
    while i < len(left) or j < len(right):
        if not i < len(left):
            res.append(right[j])
            j += 1
        elif not j < len(right):
            res.append(left[i])
            i += 1
        elif left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    return res


new_list1 = [random.uniform(0, 50) for i in range(10)]
new_list2 = [random.uniform(0, 50) for i in range(100)]
new_list3 = [random.uniform(0, 50) for i in range(1000)]


print(
    '10',
    timeit.timeit(
        'merge_sort(new_list1[:])',
        globals=globals(),
        number=1000),
    '100',
    timeit.timeit(
        'merge_sort(new_list2[:])',
        globals=globals(),
        number=1000),
    '1000',
    timeit.timeit(
        'merge_sort(new_list1[:])',
        globals=globals(),
        number=1000))

#10 0.013527099999999986 100 0.2175002 1000 0.013397400000000004