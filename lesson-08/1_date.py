class Date:
    """Incorrect mask. Usage: Date.str_to_num('DD-MM-YYYY') """
    def __init__(self, string):
        self.date_str = string

    def __str__(self):
        """Returns tuple of integers (day, month, year) via str_to_num() method """
        return str(Date.str_to_num(self.date_str))

    @classmethod
    def str_to_num(cls, string):
        """Returns tuple of integers (day, month, year) """
        if Date.validate(string):
            day, month, year = (int(el) for el in string.split('-'))
            return day, month, year

    @staticmethod
    def validate(string):
        """Returns True or False + errors output """
        try:
            day, month, year = (int(el) for el in string.split('-'))
        except ValueError:
            print(Date.__doc__)
        else:
            if day > 31 or day < 1:
                print(f'Incorrect day number: {day} in date {string}')
                return False
            elif month > 12 or month < 1:
                print(f'Incorrect month number: {month} in date {string}')
                return False
            elif year > 3000 or year < 1:
                print(f'Incorrect year number: {year} in date {string}')
                return False
            else:
                return True


# print object
print(Date('15-12-2020'))
print('\n')
# print via class method
print(Date.str_to_num('30-06-2020'))
print('\n')
# validate samples
print(Date.validate('05-12-2020'))
print('\n')
print(Date.validate('00-12-2020'))
print('\n')
print(Date.validate('09-13-2020'))
