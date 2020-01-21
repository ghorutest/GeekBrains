def write_nums(file, s):
    with open(file, 'w', encoding='utf-8') as file:
        for n in s:
            file.write(str(n) + ' ')


def read_and_sum(file):
    with open(file, 'r', encoding='utf-8') as file:
        num_list = file.read().split()
        print(sum([int(i) for i in num_list]))


file_name = '5_count_in_file.txt'
string = [1, 2, 3, 4, 5, 6]

write_nums(file_name, string)
read_and_sum(file_name)
