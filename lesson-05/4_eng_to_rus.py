def translate(string):
    num_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    for key, value in num_dict.items(): 
        if string in key:
            return value


def eng_to_rus():
    string = []
    with open('4_eng_to_rus.txt', 'r', encoding='utf-8') as file:
        for line in file:
            string.append(f'{translate(line.split()[0])} {" ".join(line.split()[1:])}\n')

    with open('4_eng_to_rus_t.txt', 'w', encoding='utf-8') as file:
        for line in string:
            file.write(line)


eng_to_rus()
