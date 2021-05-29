from itertools import count
from sys import argv
from time import sleep

script_name, counts = argv

counts = int(counts)
for i in count(counts):
    if i < counts + 1000:
        print(f'{i} убей меня')
        sleep(1)
