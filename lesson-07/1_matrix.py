class Matrix:
    def __init__(self, *args):
        self.matrix = args[0]

    def __str__(self):
        return "\n".join("\t".join(str(el) for el in string) for string in self.matrix)

    def __getitem__(self, item):
        return self.matrix[item]

    def __add__(self, other):
        result, el = [], []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                el.append(self.matrix[i][j] + other[i][j])
                if len(el) == len(self.matrix[0]):
                    result.append(el)
                    el = []
        return Matrix(result)


m_2x3_1 = Matrix([[31, 22], [37, 43], [51, 86]])
m_2x3_2 = Matrix([[11, 11], [11, 11], [11, 11]])
print(f'1-я матрица 2x3: \n{m_2x3_1}\n2-я матрица 2x3: \n{m_2x3_2}\nСумма: \n{m_2x3_1 + m_2x3_2}\n')

m_3x3_1 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
m_3x3_2 = Matrix([[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]])
print(f'1-я матрица 3x3: \n{m_3x3_1}\n2-я матрица 3x3: \n{m_3x3_2}\nСумма: \n{m_3x3_1 + m_3x3_2}\n')
