def int_func(no_small):
    return no_small.title()


def final_no_small(no_small_string):
    new_string = ''
    for local in no_small_string.split():
        new_string += int_func(local) + ' '
    return new_string


print(final_no_small('dfg rt ав уце ек'))
