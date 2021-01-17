goods = int(input("Введите сколько товаров "))
user_list = []
for n in range(goods):
    enter_dict = dict({'название': input("введите название "), 'цена': input("Введите цену "),
                      'количество': input('Введите количество '), 'единица измерений': input("Введите "
                                                                                             "единицу измерения ")})
    user_list.append((n, enter_dict))

print_dict = {'название': '', 'цена': '', 'количество': '', 'единица измерений': ''}

for i in range(goods):
    print_dict['название'] += print_dict[i][1].get('название') + ', '
    print_dict['цена'] += print_dict[i][1].get('цена') + ', '
    print_dict['количество'] += print_dict[i][1].get('количество') + ', '
    print_dict['единица измерений'] += print_dict[i][1].get('единица измерений') + ', '

print(user_list)
print(print_dict)
