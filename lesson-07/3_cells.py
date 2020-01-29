class Cell:
    def __init__(self, c):
        self.count = c

    def __str__(self):
        return f'{self.count}'

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        return Cell(self.count - other.count)

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(self.count // other.count)

    def make_order(self, arr):
        text = "\n".join(''.join('*' for _ in range(self.count)) for _ in range(arr // self.count))
        append = ''.join('*' for _ in range(arr - (arr // self.count * self.count)))
        return f'{text}\n{append}'


cell_1 = Cell(12)
cell_2 = Cell(5)
print(f'Клетка-1: {cell_1} ячеек\nКлетка-2: {cell_2} ячеек\nadd: {cell_1 + cell_2}\nsub: {cell_1 - cell_2}')
print(f'mul: {cell_1 * cell_2}\ntruediv: {cell_1 / cell_2}')
print(cell_2.make_order(12), '\n')
print(cell_2.make_order(6), '\n')

