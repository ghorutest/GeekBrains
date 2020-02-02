import pprint
import sys


def list_to_dict(list1, list2):
    return dict(zip(list1, list2))


def int_input(mes):
    while True:
        value = input(mes)
        try:
            result = int(value)
            return result
        except ValueError:
            pass


class Warehouse:
    """Класс для создания хранения объектов типа Scanner, Xerox, Printer в словаре в памяти
    Все объекты при создании первоначально попадают в подразделение, созданное при инициализации
    """
    def __init__(self, division):
        self.division = division
        self.stuff = {}
        self.stuff[division] = {}

    def __str__(self):
        return str(self.stuff)

    def ls(self):
        pprint.pprint(self.stuff)

    def add(self):
        while True:
            eq = int_input('Какой тип оргтехники добавить:\n1 - сканер\n2 - ксерокс (МФУ)\n3 - принтер\n')
            select = {1: 'Сканер', 2: 'Ксерокс', 3: 'Принтер'}
            try:
                equipment = select[eq]
                break
            except KeyError:
                pass

        # Проверка наличия подобных позиций, если нет - инициализация словаря
        try:
            pos = len(self.stuff[self.division][equipment])
        except KeyError:
            self.stuff[self.division][equipment] = {}
            pos = 0
        print(f'Добавление {equipment} в "{self.division}:"')

        if eq == 1:
            new = Scanner(
                input('Введите производителя: '),
                input('Введите модель: '),
                int_input('Введите стоимость (число): '),
                input('Введите разрешение модели: '),
                input('Введите тип подачи: '))
            self.stuff[self.division][equipment][pos] = new
            print(f'В "{self.division}" добавлен элемент типа "{equipment}":')
            print(' '.join(str(value) for value in self.stuff[self.division][equipment][pos].__dict__.values()))

        elif eq == 2:
            new = Xerox(
                input('Введите производителя: '),
                input('Введите модель: '),
                input('Введите стоимость (число): '),
                input('Введите скорость копирования (число страниц в минуту): '))
            self.stuff[self.division][equipment][pos] = new
            print(f'В "{self.division}" добавлен элемент типа "{equipment}":')
            print(' '.join(str(value) for value in self.stuff[self.division][equipment][pos].__dict__.values()))

        elif eq == 3:
            new = Printer(
                input('Введите производителя: '),
                input('Введите модель: '),
                input('Введите стоимость (число): '),
                input('Введите тип печати: '),
                input('Введите технологию печати: '))
            self.stuff[self.division][equipment][pos] = new
            print(f'В "{self.division}" добавлен элемент типа "{equipment}":')
            print(' '.join(str(value) for value in self.stuff[self.division][equipment][pos].__dict__.values()))

    def move(self):
        if len(self.stuff) > 1:
            count = 1
            select_div, select_type, select_el = [], [], []
            print('Подразделения хранения (эксплуатации):')
            for division in self.stuff:
                select_div.append([count, division])
                print('\t', count, division)
                count += 1
            div = int(input('Введите номер подразделения-источника для перемещения остатков: '))

            count = 1
            old_div = select_div[div - 1][1]
            for equipment in self.stuff[old_div]:
                select_type.append([count, equipment])
                print('\t', count, equipment)
                count += 1
            s_type = int(input('Введите номер типа остатков для перемещения: '))

            count = 1
            equipment = select_type[s_type - 1][1]
            print(f'Вывод по "{old_div}", тип: "{equipment}"')
            for el in self.stuff[old_div][equipment]:
                print('\t', count, ' '.join(str(value) for value in self.stuff[old_div][equipment][el].__dict__.values()))
                count += 1
            select_el = int(input('Введите номер позиции для перемещения: ')) - 1

            count = 1
            select_div = []
            for division in self.stuff:
                select_div.append([count, division])
                print('\t', count, division)
                count += 1
            div = int(input('Введите номер подразделения-назначения для перемещения: '))
            new_div = select_div[div - 1][1]
            # Проверка наличия подобных позиций, если нет - инициализация словаря
            try:
                pos = len(self.stuff[new_div][equipment])
            except KeyError:
                self.stuff[new_div][equipment] = {}
                pos = 0
            self.stuff[new_div][equipment][pos] = self.stuff[old_div][equipment].pop(select_el)
            if len(self.stuff[old_div][equipment]) == 0:
                _ = self.stuff[old_div].pop(equipment)
            print(f'Объект типа "{equipment}" перемещён из {old_div} в {new_div}')
        else:
            print(f'Нет подразделений для перемещения:')
            self.divs()

    def cmd(self):
        self.help()
        while True:
            try:
                exec('self.' + input() + '()')
            except AttributeError:
                pass
            except SyntaxError:
                pass

    def stat(self):
        divisions, eq, count = 0, 0, 0
        for division in self.stuff:
            divisions += 1
            for equipment in self.stuff[division]:
                eq += 1
                for _ in self.stuff[division][equipment]:
                    count += 1
        print(f'\tПодразделений хранения (эксплуатации): {divisions}')
        print(f'\tТипов оборудования: {eq}')
        print(f'\tКоличество оборудования: {count}')
        try:
            print(f'\t\tИз них сканеров: {len(self.stuff[division]["Сканер"])}')
        except KeyError:
            pass
        try:
            print(f'\t\tИз них ксероксов: {len(self.stuff[division]["Ксерокс"])}')
        except KeyError:
            pass
        try:
            print(f'\t\tИз них принтеров: {len(self.stuff[division]["Принтер"])}')
        except KeyError:
            pass

    def divs(self):
        count = 1
        print('Подразделения хранения/эксплуатации (divadd - добавить подразделение):')
        for division in self.stuff:
            print('\t', count, division)
            count += 1

    def divadd(self):
        division = input('Введите название нового подразделения: ')
        try:
            len(self.stuff[division])
        except KeyError:
            self.stuff[division] = {}
        print(f'Добавлено подразделение: {division}')

    def divls(self):
        count = 1
        select_div, select_type = [], []
        print('Подразделения хранения (эксплуатации):')
        for division in self.stuff:
            select_div.append([count, division])
            print('\t', count, division)
            count += 1
        div = int(input('Введите НОМЕР подразделения для вывода остатков: '))

        count = 1
        division = select_div[div - 1][1]
        if len(self.stuff[division]) > 0:
            for equipment in self.stuff[division]:
                select_type.append([count, equipment])
                print('\t', count, equipment)
                count += 1
            s_type = int(input('Введите НОМЕР типа остатков для вывода: '))

            count = 1
            equipment = select_type[s_type - 1][1]
            print(f'Вывод по "{division}", тип: "{equipment}"')
            for el in self.stuff[division][equipment]:
                print('\t', count, ' '.join(str(value) for value in self.stuff[division][equipment][el].__dict__.values()))
                count += 1
        else:
            print(f'\tВ "{division}" нет элементов')

    def help(self):
        print('add - добавить ед. хранения\n'
              'move - перемещение ед. хранения между подразделениями\n'
              'stat - вывести статистику склада\n'
              'divs - вывести список подразделений\n'
              'divadd - добавить подразделение\n'
              'divls - показать остатки хранения подразделений\n'
              'help - справка\n'
              'quit - выход')

    def quit(self):
        sys.exit()


class Equipment:
    def __init__(self, manufacturer, model, cost):
        self.model = model
        self.manufacturer = manufacturer
        self.cost = cost


class Scanner(Equipment):
    def __init__(self, manufacturer, model, cost, resolution, feed_type):
        super().__init__(manufacturer, model, cost)
        self.resolution = resolution
        self.feed_type = feed_type

    def __str__(self):
        return str(list_to_dict(
            ['manufacturer', 'model', 'cost', 'resolution', 'feed_type'],
            [self.manufacturer, self.model, self.cost, self.resolution, self.feed_type]))


class Xerox(Equipment):
    def __init__(self, manufacturer, model, cost, copy_speed):
        super().__init__(manufacturer, model, cost)
        self.copy_speed = copy_speed

    def __str__(self):
        return list_to_dict(
            ['manufacturer', 'model', 'cost', 'copy_speed'],
            [self.manufacturer, self.model, self.cost, self.copy_speed])


class Printer(Equipment):
    def __init__(self, manufacturer, model, cost, color_print, print_type):
        super().__init__(manufacturer, model, cost)
        self.color_print = color_print
        self.print_type = print_type

    def __str__(self):
        return list_to_dict(
            ['manufacturer', 'model', 'cost', 'color_print', 'print_type'],
            [self.manufacturer, self.model, self.cost, self.color_print, self.print_type])


wh = Warehouse('Главный склад')
wh.cmd()
