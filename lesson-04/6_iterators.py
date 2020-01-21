from itertools import count, cycle


def count_f():
    start = int(input("Стартовое число: "))
    stop = int(input("Конечное число число: "))

    for el in count(start):
        if el > stop:
            break
        else:
            print(el)


def cycle_f():
    c = 0
    stop = int(input("Сколько сиволов ряда 'ABCD...' выводить: "))
    for el in cycle("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        if c >= stop:
            break
        print(el)
        c += 1


def case():
    c = input('Введите "1" для запуска Cycle() или "2" для запуска Count() ')
    try:
        if int(c) == 1: cycle_f()
        elif int(c) == 2: count_f()
    except:
        pass


case()
