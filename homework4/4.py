old_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([el for local, el in enumerate(old_list) if old_list.count(old_list[local]) < 2])
