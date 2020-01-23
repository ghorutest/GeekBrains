def read_and_sum():
    with open('6_total_hours.txt', 'r', encoding='utf-8') as file:
        keys, totals = ([] for _ in range(2))
        for line in file:
            keys.append(line.split()[0])
            totals.append(
                sum([int(line.split()[i].split('(')[0]) for i in range(1, 4) if line.split()[i].split('(')[0] != '-']))
        return dict(zip(keys, totals))


print(read_and_sum())
