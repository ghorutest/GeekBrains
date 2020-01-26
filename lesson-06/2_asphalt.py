class Road:
    """Для расчета массы асфальта для строитества дороги тебуется:
    длина, м (int / float)
    ширина, м (int / float)
    Метод build() выводит на экран:
    Потребность асфальта в тонннах (float)
    """
    def __init__(self, ln, wd):
        self._length = ln
        self._width = wd

    def build(self):
        print(self._length * self._width * 25 * 0.05 / 1000)


road = Road(5000, 20)
road.build()
