test_list = ['234', 324, 32.3, ['magic']]


def check_type(local_type):
    return f'{local_type} имеет тип {type(local_type)}'


for i in range(len(test_list)):
    print(check_type(test_list[i]))

input()

