mouth = int(input('Введите номер месяца '))
time_year = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
list_time_year = ['зима', 'весна', 'дето', 'осень']
if mouth > 12:
    print('Такого месяца нет')
elif mouth < 3:
    print(list_time_year[0])
    print(time_year.get(1))
elif mouth < 6:
    print(list_time_year[1])
    print(time_year.get(2))
elif mouth < 9:
    print(list_time_year[2])
    print(time_year.get(3))
elif mouth < 12:
    print(list_time_year[3])
    print(time_year.get(4))
else:
    print(list_time_year[0])
    print(time_year.get(1))


