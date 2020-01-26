from time import sleep
import sys


class TrafficLight:
    def __init__(self):
        self._color = str
        self._prev_color = 'Жёлтый'
        self._colors = ['Красный', 'Жёлтый', 'Зелёный', 'Жёлтый']
        self.rotation_err = '[СБОЙ] Нарушен порядок чередования цветов'

    def running(self, hacked=False):

        while True:

            self._color = 'Красный'
            print(f'Включаем {self._color}')
            if hacked:
                import random
                self._color = random.choice(self._colors)
                print(f'Выбран случайный цвет {self._color}')
            if self._color == 'Красный' and self._prev_color == 'Жёлтый':
                print(self._color)
                self._prev_color = self._color
            else:
                print(self.rotation_err)
                sys.exit(2)
            sleep(7)

            self._color = 'Жёлтый'
            print(f'Включаем {self._color}')
            if hacked:
                import random
                self._color = random.choice(self._colors)
                print(f'Выбран случайный цвет {self._color}')
            if self._color == 'Жёлтый' and self._prev_color == 'Красный':
                print(self._color)
                self._prev_color = self._color
            else:
                print(self.rotation_err)
                sys.exit(2)
            sleep(2)

            self._color = 'Зелёный'
            print(f'Включаем {self._color}')
            if hacked:
                import random
                self._color = random.choice(self._colors)
                print(f'Выбран случайный цвет {self._color}')
            if self._color == 'Зелёный' and self._prev_color == 'Жёлтый':
                print(self._color)
                self._prev_color = self._color
            else:
                print(self.rotation_err)
                sys.exit(2)
            sleep(7)

            self._color = 'Жёлтый'
            print(f'Включаем {self._color}')
            if hacked:
                import random
                self._color = random.choice(self._colors)
                print(f'Выбран случайный цвет {self._color}')
            if self._color == 'Жёлтый' and self._prev_color == 'Зелёный':
                print(self._color)
                self._prev_color = self._color
            else:
                print(self.rotation_err)
                sys.exit(2)
            sleep(2)


light = TrafficLight()
# 1-й вариант запуска - нормальный режим
light.running()
# 2-й вариант запуска - сбойный
# light.running(hacked=True)
