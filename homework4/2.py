old_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = [el for local, el in enumerate(old_list) if old_list[local] > old_list[local - 1] and local != 0]

print(new_list)
