class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


num_list = []
while True:
    user_input = input("Введите очередное число (или stop для выхода): ")

    if user_input == 'stop':
        break
    else:
        try:
            num_list.append(int(user_input))
        except ValueError:
            print("Вы ввели не число")
        except OwnError as err:
            print(err)

print(f'Введённый список: {num_list}')
