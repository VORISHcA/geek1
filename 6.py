class Queue:
    def __init__(self):
        self.elements = []

    def is_empty(self):  # пустая
        return self.elements == []

    def add_to_queue(self, item):  # добавление в очередь
        self.elements.insert(0, item)

    def take_from_queue(self):  # получение из очереди
        return self.elements.pop()

    def size(self):  # Размер
        return len(self.elements)


class Table:
    def __init__(self):
        self.base_queue = Queue()
        self.queue_for_revision = Queue()
        self.solved = []

    def to_base_queue(self, item):  # В очередь
        self.base_queue.add_to_queue(item)

    def to_solved(self):  # В завершенное
        if not self.base_queue.is_empty():
            self.solved.append(self.base_queue.take_from_queue())

    def again_queue(self):  # Снова в очередь
        if not self.base_queue.is_empty():
            self.queue_for_revision.add_to_queue(self.base_queue.take_from_queue())

    def from_revision_to_base(self):  # Перенести из доработки
        if not self.queue_for_revision.is_empty():
            self.base_queue.add_to_queue(self.queue_for_revision.take_from_queue())

    def from_revision_to_solved(self):  # Перенести из доработки в завершенное
        if not self.queue_for_revision.is_empty():
            self.solved.append(self.queue_for_revision.take_from_queue())

    def current_task(self):  # Решаемая задача
        return self.base_queue.elements[-1] if not self.base_queue.is_empty() \
            else print('Пусто')

    def current_revision_task(self):  # Пересматриваемая задача
        return self.queue_for_revision.elements[-1] if not self.queue_for_revision.is_empty() \
            else print('Пусто')


test = Table()

for i in range(5):
    test.to_base_queue('задача' + str(i + 1))
test.to_solved()  # Имит решения задачи
test.again_queue()  # задача 2 на пересмотр и в решенные
print('Очередь не решенных', *test.base_queue.elements)
print('Очередь на пересмотр', *test.queue_for_revision.elements)
print('Выполнены задачи', *test.solved, '\n')

test.from_revision_to_solved()
print(test.current_task())
print('Сейчас на пересмотр ')
print(test.current_revision_task())
