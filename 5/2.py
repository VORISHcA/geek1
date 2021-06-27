import collections
import functools

my_numbers = collections.defaultdict(list)
cou1, cou2 = input("Введите оба числа через пробел: ").split()
my_numbers[1] = list(cou1)
my_numbers[2] = list(cou2)

sum_16 = sum([int(''.join(i), 16) for i in my_numbers.values()])
print(f'Сумма:  {sum_16}')

mult_16 = functools.reduce(lambda a, b: a * b, [int(''.join(i), 16) for i in my_numbers.values()])
print(f'Произв:  {mult_16}')
