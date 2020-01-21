from functools import reduce


def mlt(prev_el, el):
    return prev_el * el


print(reduce(mlt, [el for el in range(100, 1001) if el % 2 == 0]))
