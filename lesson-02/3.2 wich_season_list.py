winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

while True:
    try:
        month = int(input('Введите порядковый номер месяца от 1 до 12, чтобы узнать сезон\n'))
        if month in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            break
    except:
        pass

if month in winter: print('Зима')
elif month in spring: print('Весна')
elif month in summer: print('Лето')
else: print('Осень')
