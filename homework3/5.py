def user_sum(now_sum=0):
    use_string = input('Введите числа через пробел ').split()
    print(use_string)

    for now_count in use_string:
        if now_count != '666':
            now_sum += int(now_count)
        else:
            return now_sum
    return user_sum(now_sum)


print('666 - выход')
print(f'{user_sum()} итог')




