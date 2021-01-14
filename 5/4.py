trans = {'One': 'Оне', 'Two': 'Ту', 'Three': 'тсри', 'Four': 'фо'}
new_file = []
with open('file4.txt', 'r') as old:
    new = open('file5.txt', 'w')
    for now in old.readlines():
        sp_now = now.split(' ')
        new.writelines(f'{trans[sp_now[0]]} - {sp_now[2]}')

new.close()
new = open("file5.txt", "r")
print(new.read())


