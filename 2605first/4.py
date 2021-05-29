def test1(login, paswword):              # O(n)
    if not login in users.keys():               # O(n) по всеь
        return 'Не найден'
    elif paswword != users.get(login)[0]:
        return 'Ошибка пароля'
    elif not users.get(login)[1]:
        return 'пользователь не активен'
    else:
        return 'Добро пожаловать'


def test2(login, paswword):
    counter = 0
    for i in users.keys():                      # O(2n) какое-то странное искуственное усложенение
        if login == i:
            counter += 1
    if counter == 0:
        return 'Не найден'
    if paswword != users.get(login)[0]:
        return 'Ошибка пароля'
    elif not users.get(login)[1]:
        return 'пользователь не активен'
    else:
        return 'Добро пожаловать'


users = {'123': ['1', True], '1234': ['2', True], '12345': ['3', False]}

print(test1(input('login '), input('paswword ')))
print(test2(input('login '), input('paswword ')))

print(type(users.keys()))