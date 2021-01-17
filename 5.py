
proceeds, cost = map(int, input('Введите вырку и издержку через пробел ').strip().split(" "))
if proceeds > cost:
    print(f'прибыль {proceeds -cost}')
    print(f'отношение прибыли к убытку 1 к {round(proceeds / cost)}')
else:
    print(f'убыток {cost - proceeds}')

people = int(input('Введите число сотрудников '))
print(f'На одного сотрудника приходится {proceeds // people}')
