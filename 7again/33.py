import re


class Cell:
    def __init__(self, cout_cell):
        self.cout_cell = int(cout_cell)

    def __str__(self):
        return self.cout_cell * "*"

    def __add__(self, other):
        return Cell(self.cout_cell + other.cout_cell)

    def __truediv__(self, other):
        return Cell(round(self.cout_cell // other.cout_cell))

    def __sub__(self, other):
        return self.cout_cell - other.cout_cell if self.cout_cell > other.cout_cell else print('Я хз как в минус')

    def __mul__(self, other):
        return Cell(int(self.cout_cell * other.cout_cell))

    def make_order(self, count_in_str):
        row = ''
        for i in range(int(self.cout_cell / count_in_str)):
            row += f'{"*" * count_in_str} \n'
        row += f'{"*" * (self.cout_cell % count_in_str)}'
        return row


cells1 = Cell(14)
cells2 = Cell(13)
print(cells1)
print(cells1 + cells2)
print(cells1 - cells2)
print(cells1 * cells2)
print(cells1 / cells2)
print(cells2.make_order(5))
print(cells1.make_order(10))

