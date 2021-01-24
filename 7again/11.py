class Matrix:
    def __init__(self, matr):
        self.matr = matr

    def __str__(self):
        simple_print = ''
        for strin in self.matr:
            for el in strin:
                simple_print += f'{el} '
            simple_print += '\n'
        return simple_print

    def __add__(self, other):
        matr = self.matr
        if len(matr[0]) == len(other[0]) and len(matr) == len(other):
            for i in range(len(matr)):
                for l in range(len(matr[0])):
                    matr[i][l] = matr[i][l] + other[i][l]
        else:
            print('У вас матрицы разные')
        return self.matr


M = Matrix([[12, 2], [32, 3]])
print(M)
M + [[13, 43], [73, 8]]
print(M)
