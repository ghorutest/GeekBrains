def salary_stats():
    employee = []
    with open('3_salary_stats.txt', 'r', encoding='utf-8') as file:
        for line in file:
            employee.append(line.split())

    average = sum([float(sal[1]) for sal in employee]) / len(employee)
    print(f'Сотрудников: {len(employee)} средний оклад: {average:.2f}')

    salary_more = "\n".join([sal[0] for sal in employee if float(sal[1]) < 20000])
    print(f'Оклад более 20 000 у следующих сотрудников:\n{salary_more}')


salary_stats()
