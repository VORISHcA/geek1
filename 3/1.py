"""
Задание 1.
Реализуйте свои пользовательские функции, в которых реализуйте:
a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
import time


test_dict = dict((int(n), int(n)) for n in range(100000000))
test_list = list((int(n)) for n in range(100000000))


def time_c(func):
    def wrapper(n):
        start = time.time()
        func(n)
        end = time.time()
        return end - start
    return wrapper


@time_c
def list_pull(creation_list):
    list1 = []
    for i in creation_list:
        list1.append(i)
    return list1


@time_c
def dict_pull(creation_dict):
    dict1 = {}
    for key, value in creation_dict.items():
        dict1[key] = value
    return dict1


@time_c
def list_quest(creation_list):
    creation_list.index(99990000)


@time_c
def dict_quest(creation_dict):
    creation_dict.get(99990000, 0)


@time_c
def list_clear(creation_list):
    return creation_list.clear()


@time_c
def dict_clear(creation_dict):
    return creation_dict.clear()

'''
print(list_pull(test_list))  
# 0.5546271800994873
print(dict_pull(test_dict))  
# 0.7591712474822998 
print(list_clear(test_list))  
# 0.09502100944519043
print(dict_clear(test_dict))  
# 0.11502575874328613 +- одинаково
'''


print(list_quest(test_list))
# 0.9314742088317871
print(dict_quest(test_dict))
# 0.0
# Всегда 0.0, почему?
