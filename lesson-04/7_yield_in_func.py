from itertools import count

limit = 15


def fact(n):
    result = 1
    for number in count(1):
        if number > n:
            break
        result *= number
        yield result, number


for res, num in fact(limit):
    print(f'{num}! = {res}')
