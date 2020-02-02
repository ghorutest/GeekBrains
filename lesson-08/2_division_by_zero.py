class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    try:
        x, y = (int(el) for el in input("Делимое и делитель через пробел (Ctrl+C, Enter для выхода): ").split())
        try:
            result = x / y
        except ZeroDivisionError:
            print("Вы делите на ноль")
        except OwnError as err:
            print(err)
        else:
            print(f"Результат деления: {result:.03f}")
    except ValueError:
        print('Введены неверные данные')
