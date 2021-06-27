def n_sum(num):
    if num == 0:
        return 0
    else:
        sum = 1 + n_sum(num - 1) / - 2
        return sum


print(n_sum(int(input(f'Число '))))
