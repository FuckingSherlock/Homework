class ComplexNumber(complex):
    def __init__(self, *args):
        self.com = complex(*args)

    def __add__(self, other):
        print(self.com + other)

    def __mul__(self, other):
        print(self.com * other)


com1 = ComplexNumber(3, 5)
com2 = ComplexNumber(4, 2)

com1 + com2
com1 * com2
