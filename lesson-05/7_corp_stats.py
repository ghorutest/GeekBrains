import json


def list_to_dict(list1, list2):
    return dict(zip(list1, list2))


def read_and_sum():
    with open('7_corp_stats.txt', 'r', encoding='utf-8') as file:
        p_corps, p_corps_profit, unp_corps, unp_corps_loss = ([] for _ in range(4))

        for line in file:
            line_list = line.split()
            corp_name = line_list[0]
            profit = int(line_list[2]) - int(line_list[3])
            if profit >= 0:
                print(f'{corp_name} прибыль: {profit}')
                p_corps.append(corp_name)
                p_corps_profit.append(profit)
            else:
                print(f'{corp_name} убыток: {profit}')
                unp_corps.append(corp_name)
                unp_corps_loss.append(profit)

        print(f'\nСредняя прибыль: {sum(p_corps_profit)/len(p_corps_profit):.2f}')

        with open('7_corp_stats.json', 'w', encoding='utf-8') as f:
            json.dump(
                [list_to_dict(p_corps, p_corps_profit),
                    list_to_dict(unp_corps, unp_corps_loss)], f, indent=4, ensure_ascii=False)


read_and_sum()
