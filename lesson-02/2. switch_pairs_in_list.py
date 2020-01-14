list_main = input ('Введите спиок через запятую\n').split(',')
list_before = list(list_main)

list_len = len(list_main)
even = True if (list_len % 2) == 0 else False

if not even:
    list_len = list_len - 1
    print (f'Нечётная длина, игнорируем последний элемент \'{list_main[list_len]}\'\n')

for pair in range(0, list_len, 2):
    tmp = list_main[pair]
    list_main[pair] = list_main[pair + 1]
    list_main[pair + 1] = tmp
    pair += 1

print (f'До:    {list_before}\nПосле: {list_main}')
