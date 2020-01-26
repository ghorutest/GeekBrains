class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        # доступ к self.title суперкласса
        print(f'Используется: {self.title}\tПишем ручкой')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        # доступ к self.title суперкласса
        print(f'Используется: {self.title}\tРисуем карандашом')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        # доступ к self.title суперкласса
        print(f'Используется: {self.title}\tПомечаем маркером')


black_pen = Pen('Черная ручка')
black_pen.draw()
yellow_pencil = Pencil('Жёлтый карандаш')
yellow_pencil.draw()
blue_handle = Handle('Синий маркер')
blue_handle.draw()
