def one_string(name, surname, y_birth, city, email, phone):
    """Returns arguments as a string"""
    return (f"{name} {surname} {str(y_birth)} {city} {email} {phone}")

print(one_string(name = 'Владимир',
            surname = 'Мономах',
            y_birth = 1053,
            city = 'Киев',
            email = 'monomah@kievan_rus.ru',
            phone = '+495 111-22-33'))
