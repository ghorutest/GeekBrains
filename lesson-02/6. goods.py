wh, names, costs, stocks, units = ([] for i in range(5))

while True:
    pos = len(wh)
    names.append(input(f'Введите название товара №{pos + 1}\n'))
    costs.append(int(input(f'Цена еденицы {names[pos]} (только число)\n')))
    stocks.append(int(input(f'Остаток на складе {names[pos]} (только число)\n')))
    units.append(input(f'Единица измерения {names[pos]}\n'))

    product = (pos + 1, {'Название':names[pos], 'Цена':costs[pos], 'Остаток':stocks[pos], 'Единица измерения':units[pos]})
    wh.append(product)

    if input(f'Закончить вводи вывeсти анализ? (y - закончить)\n') == 'y':
        break

wh_stat = {'Название': list(set(names)), 'Цена': list(set(costs)), 'Остаток': list(set(stocks)), 'Единица измерения': list(set(units))}
print(wh, '\n', wh_stat)
