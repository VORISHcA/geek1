from collections import deque, Counter


def tree(my_str):
    count = Counter(my_str)
    sort = deque(sorted(count.items(), key=lambda item: item[1]))
    # подсчет кол-ва встречаемости символа в строке
    while len(sort) > 1:
        weight = sort[0][1] + sort[1][1]
        add = {0: sort.popleft()[0],
                1: sort.popleft()[0]}
        # новый элемент в sort
        for i, freq in enumerate(sort):
            if weight > freq[1]:
                continue
            else:
                sort.insert(i, (add, weight))
                break
        else:

            sort.append((add, weight))
        print(sort)

    return sort[0][0]


code_table = dict()


def show(haf_tree, path=''):
    if not isinstance(haf_tree, dict):
        code_table[haf_tree] = path
    else:
        show(haf_tree[1], path=f'{path}1')
        show(haf_tree[0], path=f'{path}0')  # рекурсия, если словарь еще существует


test = input('Строка ')

show(tree(test))

for i in test:
    print(f'{code_table[i]} ')
