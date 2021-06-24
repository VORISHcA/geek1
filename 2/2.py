#Посчитать четные и нечетные цифры введенного натурального числа.


def numbers(lost, odd=[], noodd=[]):
    if lost == 0:
        return print(f'Нечетные и четные ({len(odd)}, {len(noodd)})')

    else:
        last = lost % 10
        if last % 2 == 0:
            noodd.append(last)

        else:
            odd.append(last)
        lost = lost // 10
        return numbers(lost)


numbers(int(input('введите число')))
