second = int(input('Введите секунды '))
hour = second // 3600
minute = (second % 3600) // 60
second = second % 60
print(f'В привычном виде {hour}:{minute}:{second}')