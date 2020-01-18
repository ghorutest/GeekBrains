n = 20

def fact(n):
    res = 1
    for num in range(1, n + 1):
        res *= num
        yield res, num

for res, num in fact(n):
    print(f'{num}! = {res}')
