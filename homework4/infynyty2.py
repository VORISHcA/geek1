from itertools import cycle
import time

time_dead = time.time() + 10
test_list = ['раз', 'Два', 'Три', 'Хрюшка', 'Поросюшка']

for i in cycle(test_list):
    print(i)
    if time.time() > time_dead:
        break
