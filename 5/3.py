with open('file3.txt', 'r', encoding="utf-8") as local_file:
    all_str = local_file.readlines()
    all_m = 0
    for now_str in all_str:
        sp_str = now_str.split()
        if int(sp_str[1]) < 20000:
            print(f'{sp_str[0]} получает меньше 20000')
        all_m += int(sp_str[1])

print(f'Средний оклад {all_m / len(all_str)}')
