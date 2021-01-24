text = ' '
with open(r"file1.txt", "w") as local_file:
    while text != '':
        text = input('Пишите ')
        local_file.writelines(text + '\n')

local_file.close()
local_file = open("file1.txt", "r")
print(local_file.readlines())
local_file.close()




