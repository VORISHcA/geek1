def my_func(*counts):
    return counts[0] + counts[1] + counts[2] - min(counts)


print(my_func(3, 5, 7))
