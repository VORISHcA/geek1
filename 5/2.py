local_file = open('file2.txt', 'r')
all_str = local_file.readlines()

print(f'{len(all_str)} всего строк')
for now_str in all_str:
    print(f'{len(now_str)} символов')
local_file.close()
