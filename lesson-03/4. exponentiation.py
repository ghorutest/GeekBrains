def exponentiation(x, y):
    """Returns a negative power of a number"""
    return x**y

def exponentiation_cycle(x, y):
    """Returns a negative power of a number"""
    res = x
    for _ in range(y + 1, 0):
        res *= x
    return (1 / res)

x = 2.5
y = -9
print(f'Result = {exponentiation(x, y)}')
print(f'Result_cycle = {exponentiation_cycle(x, y)}')
