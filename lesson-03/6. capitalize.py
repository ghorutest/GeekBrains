global string
def capitalize_first(string):
    """Uppercases olny first letter of every word in string"""
    for i in range(0, len(string)):
        string[i] = string[i][0].capitalize() + string[i][1:]
    return string


string = input("Введите слова: ").split(' ')
print(' '.join(capitalize_first(string)))
