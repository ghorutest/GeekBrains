def next_is_bigger(s):
    for el in s:
        try:
            if el > prev:
                yield el
        except:
            pass
        prev = el


source = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([el for el in next_is_bigger(source)])
