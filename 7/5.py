class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки1 {self.title}'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки2 {self.title}'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки3 {self.title}'


pen_test1 = Pen('ручка')
pencil_test2 = Pencil('карандаш')
handle_test3 = Handle('маркер')
print(pen_test1.draw())
print(pencil_test2.draw())
print(handle_test3.draw())