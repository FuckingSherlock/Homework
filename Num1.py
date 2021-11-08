class Matrix:
    def __init__(self, m1):
        self.matrix = m1
        self.result = []

    def __add__(self, m_add):
        self.result = [map(sum, zip(*i))
                       for i in zip(self.matrix, m_add.matrix)]
        return self

    def __str__(self):
        if self.result == []:
            self.result = self.matrix
        for row in self.result:
            print(f"|{' '.join(map(str, row))}|")
        print()


add_matrix = Matrix([[31, 22], [37, 43], [51, 86]])
matrix2 = Matrix([[3, 5], [2, 4], [-1, 64]])
add_matrix.__str__()  # вывод изначальной матрицы
add_matrix + matrix2
add_matrix.__str__()


add_matrix = Matrix([[3, 5, 8, 3]])
matrix2_2 = Matrix([[8, 3, 7, 1]])
add_matrix + matrix2_2
add_matrix.__str__()
