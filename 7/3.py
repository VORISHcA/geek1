class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name + self.surname}'

    def get_total_income(self):
        return f'{self._income.get("wage") + self._income.get("bonus")}'


test = Position('Я', 'ЯЯ', 'ЯЯЯ', 0, 50)
print(test.get_full_name())
print(test.get_total_income())
