my_list = [7, 5, 3, 3, 2]
user_count = int(input('Введите число, выход при 666 '))
while user_count != 666:

    for i in range(len(my_list)):
        if user_count >= my_list[i]:
            my_list.insert(i, user_count)
            break
    if min(my_list) > user_count:
        my_list.insert(len(my_list), user_count)

    user_count = int(input('Введите число '))

print(f'{my_list} ваш список')



