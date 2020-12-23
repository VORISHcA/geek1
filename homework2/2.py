new_item = input('Введите значение элемента, завершается при пустом значении ')
user_list = []
while new_item != '':
    user_list.append(new_item)
    new_item = input('Еще ')

'''
if len(user_list) % 2 == 0:
    user_list[::2], user_list[1::2] = user_list[1::2], user_list[::2]
else:
    baf = user_list[-1]
    del user_list[-1]
    user_list[::2], user_list[1::2] = user_list[1::2], user_list[::2]
    user_list.append(baf)
'''
now_place = 0
for i in range(len(user_list)//2):
    user_list[now_place], user_list[now_place + 1] = user_list[now_place + 1], user_list[now_place]
    now_place += 2
print(user_list)


