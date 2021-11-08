class Cell:
    def __init__(self, cells):
        self.cells = cells

    def make_order(self, num_of_cells):
        self.num_of_cells = num_of_cells
        list_cells = list(range(1, self.cells+1))
        str_cells = ''
        for i in list_cells:
            if i % self.num_of_cells == 0 and i != max(list_cells):
                str_cells += '*\n'
            else:
                str_cells += '*'
        return str_cells

    def __add__(self, other):
        return self.cells + other.cells

    def __sub__(self, other):
        if not self.cells == other.cells:
            result = self.cells - other.cells
        else:
            return 'the cells are the same'
        if result >= 0:
            return result
        else:
            return 'cannot be subtracted from less'

    def __mul__(self, other):
        return self.cells * other.cells

    def __floordiv__(self, other):
        return self.cells // other.cells

    def __truediv__(self, other):
        return round(self.cells / other.cells, 3)


cell1 = Cell(17)
cell2 = Cell(300)

print(cell1 + cell2)
print(cell2 - cell1)
print(cell2 * cell1)
print(cell2 / cell1)
print(cell2 // cell1)
print(cell1.make_order(5))
