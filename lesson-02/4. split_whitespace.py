user_list = input('Введите слова, разделяя их пробелом\n').split(' ')

for item in range(len(user_list)):
    print (f'{item + 1}. {user_list[item][:10]}')
