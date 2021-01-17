def my_func(x, y):
    local = x
    for i in range(-y - 1):
        x *= local
    return f'{round(1 / x, 10)} или 1 / {x}'


print(my_func(4, -4))

