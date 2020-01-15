x = int(input('Деление чисел.\nВведите делимое (целое число): '))

while True:
    try:
        y = int(input('Введите делитель: (целое число): '))
        if y != 0:
            break
        else:
            print('Не стоит пробовать делить на 0')
    except:
        pass

def division(x, y):
    """Returns the result of dividing two integers"""
    return(x / y)

print(f'Результат: {division(x, y):f}')
