from functools import reduce

def mult(prev_el, el):
    return prev_el * el

print(reduce(mult, [el for el in range(100, 1001) if el % 2 == 0]))
