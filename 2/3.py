def number_revers(num):
    if num == 0:
        return ' Перевернулось'
    else:
        revers = str(num % 10)
        num //= 10
        return revers + number_revers(num)


print(number_revers(int(input(f'Число '))))
