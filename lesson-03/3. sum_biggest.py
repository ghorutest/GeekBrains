def my_func(x, y, z):
    """Returns the sum of the two largest numbers"""
    sort = sorted([x, y, z])
    return sort[1] + sort[2]

print(my_func(60.5, 30.5, 2))
