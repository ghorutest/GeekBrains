def capitalize_first():
    """Uppercases olny first letter of every word in string"""
    string = input("Введите слова: ").split()
    for i in range(0, len(string)):
        string[i] = string[i][0].capitalize() + string[i][1:]
    return string

print(' '.join(capitalize_first()))
