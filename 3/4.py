"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносить ее в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.
Задание творческое. Здесь нет жестких требований к выполнению.
"""

import hashlib


class Cache:
    def __init__(self):
        self.cache = {}
        self.salt = 'salt'

    def cache_add(self, url):
        if not self.cache.get(url):
            self.cache[url] = hashlib.sha512(self.salt.encode() + url.encode()).hexdigest()
        else:
            print('в кэше соответствующая страница')


cache = Cache()
cache.cache_add('https://gb.ru/')
cache.cache_add('https://www.youtube.com/')
print(cache.cache)
