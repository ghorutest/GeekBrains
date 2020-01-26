class Worker:
    """Суперкласс для: Position, хранит оклады и премию
    Доступ к фин. данным через метод show_info()
    """
    def __init__(self, position, wage, bonus, name, surname):
        self._income = {"wage": wage, "bonus": bonus}
        self.name = name
        self.surname = surname
        self.position = position

    def show_info(self):
        print(f'Работник: {self.name} {self.surname} должность: {self.position}')
        print(f'Оклад: {self._income["wage"]}  премия: {self._income["bonus"]}')


class Position(Worker):
    """Класс для формирования записей сотрудников"""
    def __init__(self, position):
        self.position = position
        self.name, self.surname = self.get_full_name()
        self.wage, self.bonus = self.get_total_income()
        # передача в init суперкласса параметров для работы метода show_info()
        super().__init__(position, self.wage, self.bonus, self.name, self.surname)

    def get_total_income(self):
        self.wage = input("Введите оклад: ")
        self.bonus = input("Введите премию: ")
        return self.wage, self.bonus

    def get_full_name(self):
        self.name = input(f"Введите имя работника для должности {self.position}: ")
        self.surname = input("Введите фамилию работника: ")
        return self.name, self.surname

    def show_position(self):
        print(f'Создана должность: {self.position}')


worker_a = Position('Бухгалтер')
worker_a.show_position()  # метод класса
worker_a.show_info()  # метод суперкласса
worker_b = Position('Водитель')
worker_b.show_position()  # метод класса
worker_b.show_info()  # метод суперкласса
