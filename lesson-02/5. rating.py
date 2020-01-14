my_list = [7, 5, 5, 5, 3, 3, 2]
my_list_len = len(my_list)

while True:
    try:
        rating = int(input('Введите новый элемент рейтинга число от 1 до 9\n'))
        if rating in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            break
    except:
        pass

if my_list[0] < rating:
    insert_index = 0
    print('Вставка в начало')
else:
    for index in range(my_list_len):
        if my_list[index] < rating:
            print(f'Вставка в позицию: {index}')
            insert_index = index
            break
        elif index == my_list_len - 1:
            print('Вставка в конец')
            insert_index = my_list_len
            break

# оставил float() для контроля
my_list.insert(insert_index, float(rating))
print(my_list)
