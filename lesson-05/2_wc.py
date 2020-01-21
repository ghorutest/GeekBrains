def word_count():
    text = []

    with open('2_wc.txt', 'r', encoding='utf-8') as file:
        line_no = 0
        for line in file:
            wc = 0
            text.append(line)
            wc += len(line.split())
            line_no += 1
            print(f'Слов в {line_no} строке: {wc}')

    print(f'Всего строк: {len(text)}')


word_count()
