def table_ascii(first=32, end=128, count=0):
    if first == end:
        return
    show = f'{first} = "{chr(first)}"'
    print(show, end=' ')
    count += 1
    first += 1
    if count == 10:
        print('\n')
        count = 0
    return table_ascii(first, end, count)


table_ascii()