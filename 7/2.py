class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width * 3 * 20


test = Road(25, 10000)
print(test.mass())
