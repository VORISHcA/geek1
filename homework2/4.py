user_string = input('Введите строку со словами через пробел ')
new_list = user_string.split(' ')

for i in range(len(new_list)):
    print(f'{i+1} {new_list[i][0:10]}')