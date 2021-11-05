class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self):
        print(self._length*self._width*25*5//1000, 'т')


weight = Road(20, 5000)

weight.weight()
