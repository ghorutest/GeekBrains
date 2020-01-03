list_t = [2, '2', True, 'True', [False, 'False'], {'a', 'b', 'c'}, ('d', 'e')]

print(f'Поэлементный вывод списка\n{list_t}')
for el in list_t:
    print (type(el), ' : ', el)
