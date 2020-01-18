def keep_unique(source):
    for el in source:
        testing = el
        if len([el for el in source if el == testing]) == 1:
            yield testing

source = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([el for el in keep_unique(source)])
