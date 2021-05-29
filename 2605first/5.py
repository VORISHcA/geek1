from random import choice


class StackOfPlates:
    def __init__(self, limit):
        self.stack = [[]]
        self.limit = limit
        self.last_stack = 0

    def __str__(self):
        txt = ''
        for i in range(len(self.stack)):
            txt += f'Стопка {i + 1}:   '
        txt += '\n'
        for i in range(self.limit - 1, -1, -1):
            for value in self.stack:
                txt += f'{value[i]:<12}' if i < len(value) else '-' * 6 + ' ' * 6
            txt += '\n'
        return txt

    def is_empty(self):
        return self.stack == [[]]

    def push_in(self, elem):
        if len(self.stack[self.last_stack]) == self.limit:
            self.stack.append([])
            self.last_stack += 1
        self.stack[self.last_stack].append(elem)

    def pop_out(self):
        if not self.is_empty():
            plate = self.stack[self.last_stack].pop()
            if not self.is_empty() and not len(self.stack[self.last_stack]):
                self.stack.pop()
                self.last_stack -= 1
            return plate

    def pop_out_from_stack(self, stack_number):
        if not self.is_empty():
            plate = self.stack[stack_number - 1].pop()
            if not self.is_empty() and not len(self.stack[stack_number - 1]):
                self.stack.pop(stack_number - 1)
                self.last_stack -= 1
            return plate

    def push_in_stack(self, elem, stack):
        if not(stack < 1 or stack > self.last_stack + 1):
            if not(len(self.stack[stack - 1]) == self.limit):
                self.stack[stack - 1].append(elem)

    def get_val(self):
        return self.stack[self.last_stack][-1]

    def number_of_stacks(self):
        return self.last_stack + 1

    def last_stack_count(self):
        return len(self.stack[self.last_stack])

    def number_of_plates(self):
        return len(self.stack[self.last_stack]) + self.limit * self.last_stack

    def number_of_plates_like(self, value):
        counter = 0
        for i in self.stack:
            for j in i:
                counter = counter + 1 if j == value else counter
        return counter


rnd_plates = [choice(['1', '2', '3', '4', '5', '6', '7', '8', '9']) for _ in range(20)]

instance = StackOfPlates(4)
instance1 = StackOfPlates(4)

for i in rnd_plates:
    instance.push_in(i)

print('Колво тарелок всего: ', instance.number_of_plates())
print('колво стопок всего', instance.number_of_stacks())
print(f'Пустая ли стопка {instance.is_empty()}')
print(f'Пустая ли стопка {instance1.is_empty()}')
print('Верхняя тарелка', instance.get_val())
print('Убрать 1 тарелку ', instance.pop_out())
print(instance.push_in_stack('5', 1))
print(instance.push_in_stack('8', 3))
print('Всего 3', instance.number_of_plates_like('3'))