now_km, need_km = map(int, input('Введите первый результат и требуемый чеоез пробел').strip().split(" "))
now_day = 1
while need_km >= now_km:
    now_km *= 1.1
    now_day += 1
print(f'Достиг резальтата за {now_day}')
