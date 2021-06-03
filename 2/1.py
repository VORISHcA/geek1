"""
Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def calculator():

    operation = input('Выберете операцию +, -, *, /: ')
    print('. для выхода')
    if operation == '.':
        return 'Выход'
    else:
        if operation in '-+*':
            try:
                a, b = input('Первое и второе чило:').split()
                if operation == '+':
                    print({a + b})
                    return calculator()

                elif operation == '-':
                    print({a - b})
                    return calculator()

                elif operation == '*':
                    print({a * b})
                    return calculator()

                elif operation == '/':
                    print({a / b})
                    return calculator()
            except ValueError:
                print('Забыли число')
                return calculator()
        else:
            print('Такой операции нет')
            return calculator()


calculator()
