count = int(input('Введите n '))
now_max = 0
while count > 10:
    local_count = count % 10
    count //= count
    if local_count > now_max:
        now_max = local_count
print(f'Максильаная цифра {now_max}')



