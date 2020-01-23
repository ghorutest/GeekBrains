def read_and_sum():
    with open('6_total_hours.txt', 'r', encoding='utf-8') as file:
        keys = []
        totals = []

        for line in file:
            values = []
            line_list = line.split()

            for i in range(1, 4):
                value = line_list[i].split('(')[0]

                if value != '-':
                    values.append(int(value))

            keys.append(line_list[0])
            totals.append(sum(values))

        return dict(zip(keys, totals))


print(read_and_sum())
