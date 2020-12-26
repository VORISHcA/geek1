def two_count(x, y):
    try:
        return x / y
    except:
        return 'На ноль делить нельзя'


print(two_count(5, 10))
print(two_count(5, 0))
print(round(two_count(154, 6), 3))
