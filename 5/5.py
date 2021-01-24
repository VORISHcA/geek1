with open('file6.txt', 'w+') as local_file:
    str_counts = input('Пишите числа \n')
    local_file.writelines(str_counts)
    all_counts = str_counts.split()

print(sum(map(int, all_counts)))
