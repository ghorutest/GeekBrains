user_number = input('Введите целое число:\n')
comparison_count = 0

max_comparison = len(user_number) - 2
max = user_number[0]

if max == 9:
    print (f"Самая большая цифра в числе: {max}")

else:
    while comparison_count <= max_comparison:

        comparison_count += 1
        if user_number[comparison_count] > max: max = user_number[comparison_count]

    print (f"Самая большая цифра в числе: {max}")
