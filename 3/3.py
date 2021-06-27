"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.
Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества
Можно воспользоваться ф-цией hash() (см. материалы к уроку)
Пример:
рара - 6 уникальных подстрок
рар
ра
ар
ара
р
а
"""


def get_substrings(string):
    substrings = set()
    for i in range(1, len(string)):
        for j in range(len(string)):
            local_string = string[j:j + i]
            substrings.add(local_string)
    return substrings


result = get_substrings('papa')
print(f'Колво уникальных подстрок - {len(result)}, и сами строки:')
print('\n'.join(result))


