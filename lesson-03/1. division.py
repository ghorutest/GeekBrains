def division():
    """Returns the result of dividing two integers"""

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
    return(x / y)

print(f'Результат: {division():f}')
