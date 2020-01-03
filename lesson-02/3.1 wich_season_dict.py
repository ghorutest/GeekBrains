seasons = {'Зима': (12, 1, 2),
            'Весна': (3, 4, 5),
            'Лето': (6, 7, 8),
            'Осень': (9, 10, 11)}

while True:
    try:
        month = int(input('Введите порядковый номер месяца от 1 до 12, чтобы узнать сезон\n'))
        if month in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            break
    except:
        pass

for key, value in seasons.items(): 
    if month in value:
        print (key)
