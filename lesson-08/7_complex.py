class Complex:
    """Создает комлексное число: a+bi, например 3+6i """
    def __init__(self, string):
        if self.validate(string):
            self.a, self.b = self.parse(string)

    @staticmethod
    def validate(string):
        string = str(string)
        try:
            a, b = (int(el) for el in string.replace('i', '').split('+'))
            return True
        except ValueError:
            print(f'{string} не является корректным комплексным числом')
            return False

    @staticmethod
    def parse(string):
        a, b = (int(el) for el in string.replace('i', '').split('+'))
        return a, b

    def __add__(self, other):
        return Complex(f'{self.a + other.a}+{self.b + other.b}i')

    def __str__(self):
        return f'{self.a}+{self.b}i'

    def __mul__(self, other):
        return Complex(f'{self.a * other.a - self.b * other.b}+{self.a * other.b + self.b * other.a}i')


com_1 = Complex('11+2i')
com_2 = Complex('12+7i')

com_3 = com_1 + com_2
print(f'{com_1} + {com_2} = {com_3}')

com_4 = com_1 * com_2
print(f'{com_1} * {com_2} = {com_4}')

print(Complex.validate(com_3), Complex.validate(com_4), '\n')
print(Complex.validate('12g+7i'))
