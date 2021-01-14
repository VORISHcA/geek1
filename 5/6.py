dict_new = {}
with open('file7.txt', 'r', encoding="utf-8") as file:
    all_str = file.readlines()
    for str_now in all_str:
        summ = 0
        for all_sp in str_now.split():
            try:
                summ += int(all_sp.split('(')[0])
            except Exception:
                pass

        dict_new[str_now.split()[0]] = summ

    print(f'Общее количество часов по предмету - \n {dict_new}')