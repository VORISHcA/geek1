from abc import ABC, abstractmethod


class Textil(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def count_cloth(self):
        pass


class Coat(Textil):
    def __init__(self, name, width):
        super().__init__()
        self.name = name
        self.width = int(width)

    @property
    def count_cloth(self):
        return self.width / 6.5 + 0.5

    def __str__(self):
        return f'Ткани в {self.name} вот стока {self.count_cloth}'


class Jacket(Textil):
    def __init__(self, name, height):
        super().__init__()
        self.name = name
        self.height = int(height)

    @property
    def count_cloth(self):
        return self.height * 2 + 0.3

    def __str__(self):
        return f'Ткани в {self.name} вот стока {self.count_cloth}'


coat = Coat('bobs', 3)
jacket = Jacket('bibs', 4)
print(coat)
print(jacket)
test = round(jacket.count_cloth + coat.count_cloth, 2)
print(test)

