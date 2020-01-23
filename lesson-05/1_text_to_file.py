def input_string():
    print('Начало ввода данных, пустая строка - выход:')
    text = []

    while True:
        string = input()
        if string == '':
            break
        text.append(string)

    with open('1_text_to_file.txt', 'w', encoding='utf-8') as file:
        for line in text:
            file.write(line + '\n')


input_string()
