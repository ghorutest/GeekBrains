seconds = int(input('Введите целое число секунд - меньньше, чем в сутках от 1 до 86 400:\n'))
hours = 0
minutes = 0
error_message = 'Проверьте введённые данные - целое число от 1 до 86 400'
error = False

if seconds < 0:
    error = True
    print (error_message)

elif seconds > 86400:
    error = True
    print (error_message)

if not error:

    if seconds > 3600:
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60

    elif seconds > 60:
        minutes = seconds // 60
        seconds = seconds % 60

    print (f'Время в ЧЧ:ММ:СС: {hours:02}:{minutes:02}:{seconds:02}')
