user_string = input('Введите слова, разделяя их пробелом\n')
user_list = user_string.split(' ')
list_len = len(user_list)

for item in range(list_len):
    item_shorted = user_list[item][:10]
    print (f'{item + 1}. {item_shorted}')
